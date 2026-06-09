from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password = ''
database = 'bd_base_pedidos'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

try:
    df_clientes = pd.read_sql('tb_clientes', engine)
    df_pedidos = pd.read_sql('tb_pedidos', engine)
    df_itens = pd.read_sql('tb_itens', engine)
    df_produtos = pd.read_sql('tb_produtos', engine)

except Exception as e:
    print(f'Erro de conexão: {e}')


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


    df_cidades = df_dados.query(
        'cidade == "Sao Paulo" or cidade == "Curitiba"' 
    )


    print('\nRelatório de pedidos realizados por clientes da cidade de São Paulo e Curitiba ')
    print(
        df_cidades[
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