#!/usr/bin/env bash
set -euo pipefail

# Cargá la key desde donde prefieras (keychain, 1Password, .env privado, etc.)
# Ejemplos (elegí uno y borrá los otros):
# export SHODAN_KEY="$(security find-generic-password -a "$USER" -s SHODAN_KEY -w)"
# export SHODAN_KEY="$(op read op://Personal/Shodan/key)"
# source /ruta/privada/.env

exec "/Users/nicktus/Code/shodan_env/bin/python" "/Users/nicktus/Code/shodan_mcp.py"
