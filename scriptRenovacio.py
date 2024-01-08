import os
import shutil
import subprocess
from datetime import datetime, timedelta
import time

# Configuración
cert_paths = ["/ruta/al/certificado1.pem", "/ruta/al/certificado2.pem"]  # Rutes als certificats
proxy_cert_path = "/ruta/al/proxy/certificados/"  # Ruta en el servidor proxy
check_interval = 3600 
last_modified_times = {}


for path in cert_paths:
    if os.path.exists(path):
        last_modified_times[path] = os.path.getmtime(path)

# Hauria de ser un parámetre d'entrada proxy_cert_path i cert_paths
# Gestionar les excepcions amb Try i Except
def copy_certificates():
    for path in cert_paths:
        if os.path.exists(path):
            # Gestionar les excepcions amb Try i Except
            shutil.copy2(path, proxy_cert_path)
            print(f"Copiado {path} al proxy")

def reload_proxy():
    print("Recargando el servidor proxy")

# Bucle principal
while True:
    for path in cert_paths:
        if os.path.exists(path) and os.path.getmtime(path) > last_modified_times[path]:
            print(f"Detectado cambio en {path}")
            copy_certificates()
            reload_proxy()
            last_modified_times[path] = os.path.getmtime(path)
    time.sleep(check_interval)

# Agrupar les funcions i les crides -- Kanban
    # Desde crontab cridar/executar al script i en el script contrrolar dates vigents i si toca o no renovar