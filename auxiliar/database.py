from sqlalchemy import create_engine
import os

def conecta_banco():
    # variáveis de conexão
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    #URL de conexão com o banco
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    return engine
    #Fim da função
