# Dockerfile pour l'API FastAPI (Backend)

# Étape 1: Utilisation de l'image officielle Python comme base
FROM python:3.10-slim

# Étape 2: Définir le répertoire de travail
WORKDIR /app

# Étape 3: Copier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4: Copier le code source de l'API dans le conteneur
COPY . .

# Étape 5: Exposer le port 8000
EXPOSE 8000

# Étape 6: Commande pour démarrer l'application FastAPI avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
