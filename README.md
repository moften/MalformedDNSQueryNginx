# MalformedDNSQueryNginx
# m10sec@proton.me
CVE-2021-23017 Malformed DNS Query PoC


Explanation of PoC:

The script uses Scapy to generate and send a DNS query to specific server.
The qname field of the DNS query is filled with a string of 300 repeated “A” characters, creating a malformed request.
While this PoC does not directly exploit Nginx, it demonstrates how malformed or unexpected input can be used in a network interaction, potentially leading to misconfigurations being revealed.

CVE-2021-23017: Una vulnerabilidad en el resolvedor DNS de NGINX que podría permitir a un atacante remoto provocar una denegación de servicio o ejecutar código arbitrario mediante respuestas DNS especialmente diseñadas. 
# Uso

pip install scapy

python3 dns_test.py


# Uso y advertencias
¿Qué hace este script?
Envía una consulta DNS con un nombre de dominio de 300 caracteres.
Puede utilizarse para probar la resistencia de servidores DNS o aplicaciones que dependen de estos, como NGINX.

# Advertencia
⚠ Este script debe ejecutarse solo en entornos de prueba.
⚠ No lo uses en servidores públicos sin autorización, ya que podría interpretarse como una actividad maliciosa.
