# Utilisez une image de python de base
FROM python:3.9-slim-buster

# Définissez le répertoire de travail
WORKDIR /app

COPY . .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt


# Démarrez l'application
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]
