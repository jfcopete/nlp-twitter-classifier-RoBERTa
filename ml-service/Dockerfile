# Utilizar una imagen base ligera de Python
FROM python:3.10-slim

# Etiqueta para describir la imagen
LABEL description="Sentiment Analysis API using FastAPI"
# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt primero para aprovechar el cacheo de Docker
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 6000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
