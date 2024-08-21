from decouple import config
import requests
import os
import random
import string
import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Variables de entorno para las URL
auth_url = os.getenv('AUTH_URL', config('AUTH_URL'))
greeting_url = os.getenv('GREETING_URL', config('GREETING_URL'))

# Generar un usuario y clave aleatorios
def generate_random_credentials(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

usuario = generate_random_credentials()
clave = generate_random_credentials()

# Obtener el token de autenticación
def get_auth_token(auth_url, usuario, clave):
    try:
        response = requests.post(auth_url, json={'usuario': usuario, 'clave': clave})
        response.raise_for_status()  # Lanza una excepción si el estatus no es 2xx
        return response.json().get('token')
    except requests.exceptions.RequestException as e:
        logger.error(f"Error de autenticación: {e}")
        raise

# Invocar el servicio de saludo
def greet_user(greeting_url, token, nombre):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f"{greeting_url}?nombre={nombre}", headers=headers)
    response.raise_for_status()
    return response.text

def main():
    try:
        logger.info("Generando credenciales aleatorias")
        logger.info(f"Usuario: {usuario}")
        logger.info(f"Clave: {clave}")

        logger.info("Obteniendo token de autenticación")
        token = get_auth_token(auth_url, usuario, clave)

        logger.info("Invocando servicio de saludo")
        greeting = greet_user(greeting_url, token, usuario)  # Usamos el usuario como nombre

        logger.info(f"Respuesta del servidor: {greeting}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error en la comunicación con el servidor: {e}")

if __name__ == "__main__":
    main()
