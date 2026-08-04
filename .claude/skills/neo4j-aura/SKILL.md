---
name: neo4j-aura
description: Connect to a Neo4j AuraDB (or any Bolt/neo4j-protocol) database and run Cypher queries. Use whenever the user wants to query, inspect, or write to their Neo4j graph — running Cypher, checking connectivity, listing labels/relationship types, exploring the schema, or verifying the AuraDB keep-alive is working. Triggers on mentions of Neo4j, AuraDB, Cypher, graph database, "run a query against the graph", or the AURA_URI / AURA_USER / AURA_PASSWORD environment variables.
---

# Neo4j AuraDB

Run Cypher against a Neo4j / AuraDB instance from the command line.

## Prerequisites

The `neo4j` Python driver must be installed:

```bash
pip install neo4j
```

Connection details are read from environment variables (the same ones this
repo's keep-alive service uses):

| Variable        | Meaning                                             | Example                                    |
| --------------- | --------------------------------------------------- | ------------------------------------------ |
| `AURA_URI`      | Bolt/neo4j connection URI                            | `neo4j+s://xxxx.databases.neo4j.io`        |
| `AURA_USER`     | Username                                             | `neo4j`                                     |
| `AURA_PASSWORD` | Password                                             | `••••••`                                    |

If the variables are not already set, ask the user for the values or point
them at their AuraDB credentials file — **never hard-code credentials into
scripts or commit them.**

## Usage

Use the bundled `cypher.py` helper. It prints results as JSON so they are easy
to read and parse.

**Check connectivity:**

```bash
python .claude/skills/neo4j-aura/scripts/cypher.py --ping
```

**Run a read query:**

```bash
python .claude/skills/neo4j-aura/scripts/cypher.py "MATCH (n) RETURN count(n) AS nodes"
```

**Run a query with parameters** (avoids Cypher injection — always prefer this
over string-formatting values into the query):

```bash
python .claude/skills/neo4j-aura/scripts/cypher.py \
  "MATCH (p:Person {name: \$name}) RETURN p" \
  --params '{"name": "Ada"}'
```

**Write query** (the helper runs in autocommit; use `--database` to target a
non-default database):

```bash
python .claude/skills/neo4j-aura/scripts/cypher.py \
  "CREATE (p:Person {name: \$name}) RETURN p" \
  --params '{"name": "Ada"}'
```

## Common recipes

**Explore the schema** — labels, relationship types, and property keys:

```bash
python .claude/skills/neo4j-aura/scripts/cypher.py "CALL db.labels()"
python .claude/skills/neo4j-aura/scripts/cypher.py "CALL db.relationshipTypes()"
python .claude/skills/neo4j-aura/scripts/cypher.py "CALL db.schema.visualization()"
```

**Sample data from a label:**

```bash
python .claude/skills/neo4j-aura/scripts/cypher.py \
  "MATCH (n:Person) RETURN n LIMIT 5"
```

**Verify the keep-alive query** (matches what `keep_alive.py` runs):

```bash
python .claude/skills/neo4j-aura/scripts/cypher.py "RETURN datetime() AS now"
```

## Guidance

- Prefer parameterized queries (`--params`) over interpolating user input into
  the Cypher string.
- Add a `LIMIT` when exploring unknown data so you don't pull back a whole graph.
- Read queries are safe to run freely; before running a query that writes or
  deletes (`CREATE`, `MERGE`, `SET`, `DELETE`, `REMOVE`, `DROP`), confirm intent
  with the user unless they've clearly asked for that mutation.
- On `ServiceUnavailable` / `AuthError`, re-check `AURA_URI`, `AURA_USER`, and
  `AURA_PASSWORD` — these are the same failure modes the keep-alive service
  alerts on.
