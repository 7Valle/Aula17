from sqlalchemy import create_engine
import pandas as pd

from dotenv import load_dotenv
import os


load_dotenv()

# variáveis de conexão
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

try:
    df_clientes = pd.read_sql('tb_clientes', engine)
    df_pedidos = pd.read_sql('tb_pedidos', engine)
    df_itens = pd.read_sql('tb_itens', engine)
    df_produtos = pd.read_sql('tb_produtos', engine)

except Exception as e:
    print(f'Erro na conexão: {e}')

try:
    df_merge1 = pd.merge(
        df_clientes,
        df_pedidos,
        on = 'codigo_cliente'
    )

    
    df_merge2 = pd.merge(
        df_merge1,
        df_itens,
        on = 'codigo_pedido'
    )


    df_dados = pd.merge(
        df_merge2,
        df_produtos,
        on = 'codigo_produto'
    )


    df_sp = df_dados.query(
        'cidade == "Sao Paulo"' 
    )


    print('\nRelatório de pedidos realizados por clientes da cidade de São Paulo ')
    print(
        df_sp[
            [
                'codigo_cliente', 'nome', 'sobrenome', 'cidade',
                'codigo_pedido',
                'data_pedido', 'valor',
                'produto'
            ]
        ]
    )

except Exception as e:
    print(f'Erro ao relacionar os dados: {e}')