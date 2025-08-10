
FROM python:3.11-slim

WORKDIR /app
COPY keep_alive.py /app/
COPY health_check.py /app/

RUN pip install neo4j schedule requests

CMD ["python", "keep_alive.py"]
