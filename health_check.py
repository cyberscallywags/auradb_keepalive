
import sys
import os
from neo4j import GraphDatabase

AURA_URI = os.getenv("AURA_URI")
AURA_USER = os.getenv("AURA_USER")
AURA_PASSWORD = os.getenv("AURA_PASSWORD")

try:
    driver = GraphDatabase.driver(AURA_URI, auth=(AURA_USER, AURA_PASSWORD))
    with driver.session() as session:
        session.run("RETURN 1")
    print("OK")
    sys.exit(0)
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)
