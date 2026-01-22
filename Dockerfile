FROM python:3.9-alpine
# Crear usuario no root por seguridad
RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
