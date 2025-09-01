#!/usr/bin/env bash
set -euo pipefail

# Cargá la key desde donde prefieras (keychain, 1Password, .env privado, etc.)
# Ejemplos (elegí uno y borrá los otros):
# export SHODAN_KEY="$(security find-generic-password -a "$USER" -s SHODAN_KEY -w)"
# export SHODAN_KEY="$(op read op://Personal/Shodan/key)"
# source /ruta/privada/.env

# es necesario apuntar al path de python de tu env creado al comienzo, y tambien ajustar el path del MCP Server.
exec "/PATH/TO/VENV/bin/python" "/PATH/TO/MCP/shodan_mcp.py"
