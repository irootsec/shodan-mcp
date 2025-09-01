#!/usr/bin/env python3
import os
import sys
import requests
from dotenv import load_dotenv, find_dotenv
from mcp.server.fastmcp import FastMCP

# Cargar .env (busca hacia arriba en el árbol del proyecto)
load_dotenv(find_dotenv())

# Logs a stderr (nunca a stdout, que es el canal MCP)
def _log(msg: str):
    print(msg, file=sys.stderr, flush=True)

mcp = FastMCP("ShodanMCP")

def _key() -> str:
    key = os.getenv("SHODAN_KEY")
    if not key:
        # Error claro para el host/LLM (se verá como error de tool)
        raise RuntimeError("Falta SHODAN_KEY (definila en un archivo .env)")
    return key

def _get(url: str, **params) -> dict:
    try:
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        # Mensaje más legible para el agente
        status = e.response.status_code if e.response else "?"
        body = ""
        try:
            body = e.response.text[:400] if e.response is not None else ""
        except Exception:
            pass
        raise RuntimeError(f"HTTP {status} al consultar Shodan: {body}") from e
    except requests.RequestException as e:
        raise RuntimeError(f"Error de red al consultar Shodan: {e}") from e

@mcp.tool()
def shodan_lookup_ip(ip: str) -> dict:
    """Obtiene datos de Shodan para una IP pública."""
    return _get("https://api.shodan.io/shodan/host/" + ip, key=_key())

@mcp.tool()
def shodan_search_domain(domain: str, page: int = 1) -> dict:
    """Busca hosts cuyo hostname coincida con el dominio."""
    query = f"hostname:{domain}"
    return _get("https://api.shodan.io/shodan/host/search",
                key=_key(), query=query, page=page)

@mcp.tool()
def shodan_search_query(query: str, page: int = 1) -> dict:
    """Ejecuta una query DSL de Shodan (ej: 'apache country:AR')."""
    return _get("https://api.shodan.io/shodan/host/search",
                key=_key(), query=query, page=page)

if __name__ == "__main__":
    _log("ShodanMCP iniciado (dotenv cargado).")
    # stdio por defecto: Cursor lo lanza y habla por pipes
    mcp.run()