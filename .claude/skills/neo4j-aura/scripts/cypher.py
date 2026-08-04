#!/usr/bin/env python3
"""Run a Cypher query against a Neo4j / AuraDB instance and print JSON results.

Connection details come from environment variables:
    AURA_URI, AURA_USER, AURA_PASSWORD

Examples:
    python cypher.py --ping
    python cypher.py "MATCH (n) RETURN count(n) AS nodes"
    python cypher.py "MATCH (p:Person {name: \\$name}) RETURN p" --params '{"name": "Ada"}'
"""
import argparse
import json
import os
import sys

try:
    from neo4j import GraphDatabase
    from neo4j.exceptions import AuthError, Neo4jError, ServiceUnavailable
except ImportError:
    sys.exit("The 'neo4j' driver is not installed. Run: pip install neo4j")


def _serialize(value):
    """Best-effort conversion of Neo4j values into JSON-friendly structures."""
    # Nodes, Relationships, Paths expose their data via these attributes.
    if hasattr(value, "labels"):  # Node
        return {"labels": list(value.labels), "properties": dict(value)}
    if hasattr(value, "type") and hasattr(value, "nodes"):  # Relationship
        return {"type": value.type, "properties": dict(value)}
    if hasattr(value, "isoformat"):  # date/time/datetime
        return value.isoformat()
    if isinstance(value, (list, tuple)):
        return [_serialize(v) for v in value]
    if isinstance(value, dict):
        return {k: _serialize(v) for k, v in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser(description="Run a Cypher query against Neo4j/AuraDB.")
    parser.add_argument("query", nargs="?", help="Cypher query to run.")
    parser.add_argument("--params", help="Query parameters as a JSON object.")
    parser.add_argument("--database", help="Target database name (defaults to server default).")
    parser.add_argument("--ping", action="store_true", help="Just verify connectivity and exit.")
    args = parser.parse_args()

    uri = os.getenv("AURA_URI")
    user = os.getenv("AURA_USER")
    password = os.getenv("AURA_PASSWORD")

    required = (("AURA_URI", uri), ("AURA_USER", user), ("AURA_PASSWORD", password))
    missing = [name for name, value in required if not value]
    if missing:
        sys.exit(f"Missing required environment variable(s): {', '.join(missing)}")

    if args.ping:
        query, params = "RETURN 1 AS ok", {}
    else:
        if not args.query:
            sys.exit("No query provided. Pass a Cypher string or use --ping.")
        query = args.query
        try:
            params = json.loads(args.params) if args.params else {}
        except json.JSONDecodeError as e:
            sys.exit(f"--params is not valid JSON: {e}")

    session_kwargs = {"database": args.database} if args.database else {}

    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session(**session_kwargs) as session:
            result = session.run(query, params)
            rows = [{k: _serialize(v) for k, v in record.items()} for record in result]
        driver.close()
    except (ServiceUnavailable, AuthError) as e:
        sys.exit(f"Connection error: {e}")
    except Neo4jError as e:
        sys.exit(f"Query error: {e}")

    if args.ping:
        print("OK" if rows and rows[0].get("ok") == 1 else "UNEXPECTED RESPONSE")
    else:
        print(json.dumps(rows, indent=2, default=str))


if __name__ == "__main__":
    main()
