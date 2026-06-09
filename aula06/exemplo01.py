from sqlalchemy import create_engine
import pandas as pd

# Variáveis de conexão
host = 'localhost'
user = 'root'
password = ''
database = 'bd_biblioteca02'

# URL de conexão com o banco
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Obtendo os dados do banco 
try:
    # Lendo as tabelas
    df_usuarios = pd.read_sql('tb_usuarios', engine)
    df_livros = pd.read_sql('tb_livros', engine)
    df_itens_alugados = pd.read_sql('tb_itens_alugados', engine)
    df_alugados = pd.read_sql('tb_alugados', engine)

except Exception as e:
    print(f'Erro na conexão: {e}')

# Relacionando os dataframes
try:
    # Livros com itens alugados
    df_merge1 = pd.merge(
        df_livros,
        df_itens_alugados,
        on = 'id_livro'
    )
    # Quando as séries forem de nomes diferentes
    # df_merge1 = pd.merge(df_livros, df_itens_alugados, left_on = 'codigo_livro', right_on = 'livro_codigo')

    # Resultado com alugados
    df_merge2 = pd.merge(
        df_alugados,
        df_merge1,
        on = 'id_aluguel'
    )
    # Resultado atual (merge1 e alugados) com usuarios
    df_dados = pd.merge(
        df_usuarios,
        df_merge2,
        on = 'id_usuario'
    )
    #print(df_dados)

    # filtro = (
    #     (df_dados['data_devolucao'] >= '2024-11-01') & # & == AND, | == OR
    #     (df_dados['data_devolucao'] <= '2024-11-30')
    # )

    #print(filtro)

    #df_novembro = df_dados[filtro]
    #print(df_novembro)

    df_novembro = df_dados.query(
        'data_devolucao >= "2024-11-01" and data_devolucao <= "2024-11-30"'
    )

    print('\nRelatório de Livros alugados em Novembro: ')
    print(
        df_novembro[
            [
                'id_usuario', 'nome', 'cidade',
                'id_aluguel', 'data_aluguel', 'data_devolucao', 'valor',
                'id_livro', 'titulo'
            ]
        ]
    )


except Exception as e:
    print(f'Erro ao relacionar os dados: {e}')
