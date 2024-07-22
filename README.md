# Proyecto Django

Este proyecto es una aplicación web desarrollada con Django. A continuación se detallan los pasos para configurar y ejecutar el proyecto en su entorno local.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)
- virtualenv (opcional pero recomendado)

## Instalación

1. **Clonar el repositorio**
   
   ```bash
   git clone https://github.com/SeDelafuente/Automotora_ET_DJANGO.git
   cd Automotora_ET_DJANGO
   ```

2. **Crear y activar un entorno virtual**
   
   Es recomendable utilizar un entorno virtual para evitar conflictos con otras instalaciones de Python. Puedes crear y activar un entorno virtual con los siguientes comandos:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar las dependencias**

   Todas las dependencias necesarias están listadas en el archivo `requirements.txt`. Usa pip para instalarlas:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuración de la base de datos**

   Asegúrate de tener configurado tu archivo `settings.py` con la información de tu base de datos. Luego, aplica las migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario**

   Para acceder al panel de administración de Django, necesitarás crear un superusuario:

   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor de desarrollo**

   Finalmente, puedes iniciar el servidor de desarrollo para ver la aplicación en funcionamiento:

   ```bash
   python manage.py runserver
   ```

   La aplicación estará disponible en `http://127.0.0.1:8000/`.
