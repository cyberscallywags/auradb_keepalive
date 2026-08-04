import os
import smtplib
import time
from email.mime.text import MIMEText

import requests
import schedule
from neo4j import GraphDatabase
from neo4j.exceptions import AuthError, ServiceUnavailable

# --- Configuration ---
AURA_URI = os.getenv("AURA_URI", "neo4j+s://<your-instance-id>.databases.neo4j.io")
AURA_USER = os.getenv("AURA_USER", "neo4j")
AURA_PASSWORD = os.getenv("AURA_PASSWORD", "<your-password>")
KEEP_ALIVE_QUERY = "RETURN datetime()"
FREQUENCY_MINUTES = int(os.getenv("FREQUENCY_MINUTES", "500"))

# Alerting
ENABLE_SLACK = os.getenv("ENABLE_SLACK", "false").lower() == "true"
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK", "")
ENABLE_EMAIL = os.getenv("ENABLE_EMAIL", "false").lower() == "true"
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
EMAIL_TO = os.getenv("EMAIL_TO", "")

# --- Neo4j Driver ---
driver = GraphDatabase.driver(AURA_URI, auth=(AURA_USER, AURA_PASSWORD))


def send_slack_alert(message: str):
    if ENABLE_SLACK and SLACK_WEBHOOK:
        requests.post(SLACK_WEBHOOK, json={"text": message})


def send_email_alert(subject: str, body: str):
    if ENABLE_EMAIL and SMTP_USER and EMAIL_TO:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = EMAIL_TO
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_USER, EMAIL_TO, msg.as_string())
        except Exception as e:
            print(f"Failed to send email: {e}")


def keep_alive():
    """Send a lightweight query to keep AuraDB alive."""
    print("Running keep-alive query...")
    try:
        with driver.session() as session:
            result = session.run(KEEP_ALIVE_QUERY)
            for record in result:
                print(f"AuraDB keep-alive at {record[0]}")
    except (ServiceUnavailable, AuthError) as e:
        error_msg = f"ERROR: Failed to connect to AuraDB: {e}"
        print(error_msg)
        send_slack_alert(error_msg)
        send_email_alert("AuraDB Keep-Alive Failure", error_msg)


# Schedule the job
schedule.every(FREQUENCY_MINUTES).minutes.do(keep_alive)

print(
    f"Keep-alive job started. Running every {FREQUENCY_MINUTES} minutes. Press Ctrl+C to stop."
)
keep_alive()  # Run immediately at startup

while True:
    schedule.run_pending()
    time.sleep(100)
