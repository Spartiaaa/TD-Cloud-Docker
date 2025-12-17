# 2. Imports des Routeurs
from api.v1.chambre_routeur import routeur as chambre_routeur
from api.v1.client_routeur import routeur as client_routeur
from api.v1.hotel_routeur import routeur as hotel_routeur
from api.v1.reservation_routeur import routeur as reservation_routeur

# 1. Imports Base de Données
# ATTENTION : On importe Base depuis database.base (là où il est unique)
# On importe engine depuis database.session (là où est la config)
from database.base import Base
from database.session import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 3. Création des tables
# Cela va scanner tous les modèles importés via les routeurs ou explicitement
Base.metadata.create_all(bind=engine)

# 4. Application FastAPI
app = FastAPI()

# 5. Configuration CORS
# J'ai nettoyé la syntaxe de ta liste origins (il y avait un crochet en trop dans le commentaire)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 6. Enregistrement des Routeurs
app.include_router(hotel_routeur)
app.include_router(chambre_routeur)
app.include_router(client_routeur)
app.include_router(reservation_routeur)


# 7. Route de test
@app.get("/")
def read_root():
    return {
        "message": "Bienvenue sur l'API Hotel de Enzo Savoglou !",
        "docs": "Va sur /docs pour tester les endpoints",
        "Interface": "Pour tester le frontend, rend toi sur le le port 8080 !",
    }
