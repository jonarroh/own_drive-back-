# Own_drive

### Own_Drive - Backend 📁💻🔙

## Description 📝

Own_Drive es una aplicación web de almacenamiento de archivos en la nube que te permite subir, descargar y compartir tus archivos en cualquier momento y lugar. Este es el repositorio del backend de la aplicación. 🚀

Dependencias 📦

Este proyecto requiere las siguientes dependencias:

- Flask: 1.1.2 o superior 🔍
- Python: 3.7 o superior 🐍

## Instalación 🔧

1. Clonar este repositorio en tu máquina local. 💻
2. Instalar las dependencias utilizando el comando pip install -r requirements.txt. 🚀
3. Iniciar el servidor utilizando el comando python app.py. 🚀

Endpoints 🛣️
El servidor actualmente cuenta con dos endpoints:

1.  **/api/publicfiles**(GET): Este endpoint devuelve un archivo JSON con los datos de los archivos almacenados en la carpeta 'public'. 📂

2.  **/api/upload** (POST): Este endpoint permite subir un archivo a la carpeta 'public' del servidor. El archivo debe ser enviado en el cuerpo de la solicitud con el nombre de 'file'. 📤
