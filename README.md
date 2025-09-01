# MCP Shodan - Guía de Configuración y Uso

## 📋 Descripción
Este MCP (Model Context Protocol) permite integrar las capacidades de búsqueda de Shodan directamente en aplicaciones que soporten el protocolo MCP. Shodan es un motor de búsqueda para dispositivos conectados a internet.

## En funcionamiento 📹

![shodan MCP_v3](https://github.com/user-attachments/assets/8aab1054-3171-48b8-b429-9d7fc812c644)


## 🚀 Configuración Inicial

### 1. Configurar el entorno virtual
```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar la API Key de Shodan
```bash
# Crear archivo .env con tu API key de Shodan
echo 'SHODAN_KEY=TU_KEY_AQUI' > .env
```

**Nota**: Obtén tu API key gratuita en [shodan.io](https://account.shodan.io/)

### 3. Verificar la configuración
```bash
# Lanzar manualmente para verificar que no crashea
./run_shodan_mcp.sh
```

El servidor se quedará esperando conexiones MCP.

## 🔧 Herramientas Disponibles

### 1. `shodan_search_domain`
Busca hosts cuyo hostname coincida con el dominio especificado.

**Parámetros:**
- `domain` (requerido): Dominio a buscar
- `page` (opcional): Número de página (default: 1)

**Ejemplo de uso:**
```json
{
  "domain": "example.com",
  "page": 1
}
```

### 2. `shodan_lookup_ip`
Obtiene datos de Shodan para una IP pública específica.

**Parámetros:**
- `ip` (requerido): Dirección IP a consultar

**Ejemplo de uso:**
```json
{
  "ip": "8.8.8.8"
}
```

### 3. `shodan_search_query`
Ejecuta una query DSL de Shodan con filtros avanzados.

**Parámetros:**
- `query` (requerido): Query DSL de Shodan
- `page` (opcional): Número de página (default: 1)

**Ejemplos de queries:**
- `"apache country:AR"` - Buscar servidores Apache en Argentina
- `"nginx os:linux"` - Buscar servidores Nginx en Linux
- `"port:22"` - Buscar servicios SSH

## 📊 Ejemplos de Resultados

### Búsqueda por Dominio
```json
{
  "domain": "ole.com.ar",
  "results": [
    {
      "ip": "200.32.4.13",
      "port": 80,
      "organization": "Telecom Argentina S.A.",
      "location": "Buenos Aires, Argentina",
      "services": ["Apache/2.4.41 (Ubuntu)"]
    }
  ]
}
```

### Búsqueda por IP
```json
{
  "ip": "104.26.1.93",
  "organization": "Cloudflare, Inc.",
  "location": "San Francisco, California, United States",
  "services": ["cloudflare"],
  "ports": [80, 443]
}
```

## 🛡️ Consideraciones de Seguridad

### Protecciones Comunes Detectadas
- **Cloudflare WAF**: Error 1003 - "Direct IP access not allowed"
- **Firewalls**: Puertos cerrados o filtrados
- **CDNs**: Múltiples IPs para un mismo dominio

### Información Típica Encontrada
- **Servidores web**: Apache, Nginx, IIS
- **Sistemas operativos**: Linux, Windows, FreeBSD
- **Organizaciones**: ISPs, CDNs, hosting providers
- **Ubicaciones geográficas**: País, ciudad, coordenadas

## 🔍 Casos de Uso

### 1. Reconocimiento de Infraestructura
- Identificar servicios expuestos
- Mapear la infraestructura de un dominio
- Detectar tecnologías utilizadas

### 2. Análisis de Seguridad
- Verificar puertos abiertos
- Identificar servicios no seguros
- Detectar configuraciones incorrectas

### 3. Investigación de Red
- Encontrar hosts relacionados
- Analizar patrones de tráfico
- Mapear redes corporativas

## 📝 Notas Importantes

### Limitaciones de la API Gratuita
- **Límite de consultas**: 100 consultas por mes
- **Resultados limitados**: Máximo 100 resultados por consulta
- **Sin alertas**: Las alertas requieren cuenta premium

### Mejores Prácticas
- **Rate limiting**: No hacer consultas excesivas
- **Caché**: Almacenar resultados para evitar consultas repetidas
- **Filtros**: Usar queries específicas para obtener resultados relevantes

### Troubleshooting
- **Sin resultados**: El dominio/IP puede no estar indexado
- **Error de autenticación**: Verificar la API key
- **Límite excedido**: Esperar al siguiente mes o actualizar plan

## 🔗 Enlaces Útiles

- [Documentación oficial de Shodan](https://developer.shodan.io/)
- [Shodan CLI](https://cli.shodan.io/)
- [Shodan Exploits](https://exploits.shodan.io/)
- [Shodan Maps](https://maps.shodan.io/)

## 📞 Soporte

Para problemas con la API de Shodan:
- [Shodan Support](https://support.shodan.io/)
- [Shodan Community](https://community.shodan.io/)

---

**⚠️ Aviso Legal**: Este MCP es para fines educativos y de investigación. Asegúrate de tener autorización antes de escanear sistemas que no te pertenezcan.
