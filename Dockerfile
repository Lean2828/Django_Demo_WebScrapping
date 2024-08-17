# Usar una imagen base oficial de Python
FROM python:3.11-slim

# Instalar dependencias del sistema, incluyendo gnupg
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    gnupg

# Añadir el repositorio de Google Chrome y la llave de firma
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Instalar Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Instalar ChromeDriver
RUN wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip -P /tmp/ \
    && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . /app

# Crear y activar el entorno virtual con el nombre VENV_Django_WebScrapping
RUN python -m venv /app/VENV_Django_WebScrapping
RUN . /app/VENV_Django_WebScrapping/bin/activate

# Actualizar pip dentro del entorno virtual
RUN /app/VENV_Django_WebScrapping/bin/pip install --upgrade pip

# Instalar dependencias de Python desde el archivo requirements.txt en la raíz
RUN /app/VENV_Django_WebScrapping/bin/pip install -r /app/requirements.txt

# Exponer el puerto 8000
EXPOSE 8000

# Establecer el comando de inicio ejecutando gunicorn desde el entorno virtual
CMD ["/bin/bash", "-c", ". /app/VENV_Django_WebScrapping/bin/activate && cd Django_Demo_WebScrapping && /app/VENV_Django_WebScrapping/bin/gunicorn Django_Demo_WebScrapping.wsgi:application --bind 0.0.0.0:8000"]
