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