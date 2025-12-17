from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Chaîne de connexion MySQL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://userdb:userdb@localhost/hotel_db"

# Création du moteur
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_recycle=3600
)

# Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Déclarative Base pour ORM
Base = declarative_base()  # ✅ c'est ce qu'il faut importer dans main.py

# Dépendance pour FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
