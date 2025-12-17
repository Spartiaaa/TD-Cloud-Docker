# Gestionnaire d'Hôtel API

Ce projet est une application web full-stack pour la gestion d'hôtels, de chambres, de clients et de réservations. Il est conçu avec une architecture de microservices conteneurisée à l'aide de Docker.

## 🚀 Fonctionnalités

- **Gestion des Hôtels**: CRUD pour les hôtels.
- **Gestion des Chambres**: CRUD pour les chambres, avec la possibilité de les lister par hôtel.
- **Gestion des Clients**: CRUD pour les clients.
- **Gestion des Réservations**: CRUD pour les réservations.

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript (via un serveur Apache)
- **Base de données**: MariaDB
- **Conteneurisation**: Docker & Docker Compose

## 📂 Structure du projet

Le projet est structuré comme suit :

```
.
├── backend/            # Code source du backend FastAPI
│   ├── api/            # Routeurs FastAPI
│   ├── database/       # Configuration de la base de données
│   ├── models/         # Modèles SQLAlchemy
│   ├── schemas/        # Schémas Pydantic
│   ├── services/       # Logique métier
│   ├── Dockerfile      # Dockerfile pour le backend
│   └── requirements.txt# Dépendances Python
├── frontend/           # Code source du frontend
│   ├── js/             # Fichiers JavaScript
│   ├── css/            # Fichiers CSS
│   └── index.html      # Point d'entrée du frontend
├── BDD/                # Fichiers liés à la base de données
│   └── docker-entrypoint-initdb.d/ # Scripts d'initialisation SQL
├── docker-compose.yaml # Fichier de configuration Docker Compose
└── README.md           # Ce fichier
```

## 🏁 Démarrage rapide

### Prérequis

Assurez-vous d'avoir [Docker](https://docs.docker.com/get-docker/) et [Docker Compose](https://docs.docker.com/compose/install/) installés sur votre machine.

### Installation & Lancement

1.  Clonez ce dépôt.
2.  Ouvrez un terminal à la racine du projet.
3.  Exécutez la commande suivante pour construire et démarrer les conteneurs :

    ```bash
    docker-compose up --build
    ```

L'application sera alors accessible aux adresses suivantes :

- **Frontend**: `http://localhost:8080`
- **Backend API (docs)**: `http://localhost:8000/docs`

## 📖 API Endpoints

Voici la liste des endpoints disponibles sur l'API :

### Hôtels (`/hotels`)

- `POST /`: Créer un nouvel hôtel.
- `GET /`: Lister tous les hôtels.
- `GET /{hotel_id}`: Obtenir les détails d'un hôtel spécifique.
- `DELETE /{hotel_id}`: Supprimer un hôtel.

### Chambres (`/chambres`)

- `POST /`: Créer une nouvelle chambre.
- `GET /{hotel_id}`: Lister toutes les chambres d'un hôtel spécifique.
- `PUT /{chambre_id}`: Mettre à jour une chambre.
- `GET /{chambre_id}`: Obtenir l'état d'une chambre (disponibilité).

### Clients (`/clients`)

- `POST /`: Créer un nouveau client.
- `GET /`: Lister tous les clients.
- `GET /{client_id}`: Obtenir les détails d'un client spécifique.

### Réservations (`/reservations`)

- `POST /`: Créer une nouvelle réservation.
- `GET /`: Lister toutes les réservations.
- `DELETE /{reservation_id}`: Supprimer une réservation.

## 🖥️ Frontend

Le frontend est une application JavaScript simple qui consomme l'API backend. Il permet d'effectuer les opérations de base de gestion hôtelière via une interface web. Pour y accéder, ouvrez votre navigateur à l'adresse `http://localhost:8080`.
