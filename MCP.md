# Neo4j MCP server

This repo ships a [`.mcp.json`](./.mcp.json) that wires the official
[`mcp-neo4j-cypher`](https://github.com/neo4j-contrib/mcp-neo4j) server into
Claude Code, so you can query this AuraDB instance through MCP tools (schema
introspection, read Cypher, write Cypher) instead of shelling out.

## Requirements

- [`uv`](https://docs.astral.sh/uv/) on your PATH (provides `uvx`). The server
  itself is fetched on demand by `uvx mcp-neo4j-cypher@latest` — nothing to
  install manually.

## Configuration

Connection details are read from environment variables. The `.mcp.json` maps
this repo's existing `AURA_*` vars onto the names the server expects:

| `.mcp.json` env    | Source var        | Meaning                       |
| ------------------ | ----------------- | ----------------------------- |
| `NEO4J_URI`        | `AURA_URI`        | Bolt/neo4j connection URI     |
| `NEO4J_USERNAME`   | `AURA_USER`       | Username                      |
| `NEO4J_PASSWORD`   | `AURA_PASSWORD`   | Password                      |
| `NEO4J_DATABASE`   | `NEO4J_DATABASE`  | Database name (default `neo4j`) |

Set them before launching Claude Code:

```bash
cp .env.example .env      # then edit .env with your real values
set -a; source .env; set +a
```

No credentials live in `.mcp.json` — it only references the variables, so the
file is safe to commit.

## Usage

Once the vars are set and Claude Code is (re)started in this directory, approve
the `neo4j-cypher` server when prompted. It exposes tools such as:

- `get_neo4j_schema` — labels, relationship types, and property keys
- `read_neo4j_cypher` — run a read-only Cypher query
- `write_neo4j_cypher` — run a write Cypher query

Then just ask, e.g. *"list all node labels"* or *"how many Person nodes are
there?"* and Claude will call the MCP tools.

## MCP server vs. the `neo4j-aura` skill

Both talk to the same database; pick based on how you want to work:

- **MCP server** — Claude calls native tools directly; best for interactive
  exploration and letting the model drive queries.
- **`neo4j-aura` skill** (`.claude/skills/neo4j-aura/`) — a scriptable
  `cypher.py` helper; best for reproducible CLI usage, CI, or when you don't
  want to run the MCP server.
