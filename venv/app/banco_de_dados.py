from pymongo import MongoClient

MONGODB_URI = "mongodb://localhost:27017/"
DB_NAME = "CRUD"


def conectar_db():
    try:
        client = MongoClient(MONGODB_URI)
        db = client[DB_NAME]
        collection = db.estudantes
        print("Conexão com o MongoDB estabelicida com sucesso!")
        return collection
    except Exception as e:
        print(f"Erro ao conetcar com o MongoDB: {e}")
        return None
