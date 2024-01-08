#!/bin/bash

# Detener Apache antes de la renovación del certificado
pre_renewal() {
    service apache2 stop
}

# Reiniciar Apache después de la renovación del certificado
post_renewal() {
    service apache2 start
}

# Ejecutar Certbot con los hooks definidos
renew_certificates() {
    certbot renew --pre-hook "pre_renewal" --post-hook "post_renewal"
}

# Ejecutar el script de Python para transferir los certificados
transfer_certificates() {
    /usr/bin/python3 /ruta/a/actualizar_certificados.py
}

# Lógica principal del script
pre_renewal
renew_certificates
post_renewal
transfer_certificates

echo "Proceso completado"
