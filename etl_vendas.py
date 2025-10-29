import pandas as pd  # importa a biblioteca de manipulação de dados

# Leitura dos dados de vendas
df = pd.read_csv('vendas.csv')  # lê o arquivo CSV localmente

# Renomeia uma coluna (transformação 1)
# Aqui, o nome original deve realmente existir no CSV.
# Exemplo: se a coluna original for 'valor_unitario', use esse nome.
df.rename(columns={'valor': 'preco_unitario'}, inplace=True)

#  Cria uma nova coluna com o preço acrescido de imposto (transformação 2)
df['preco_com_imposto'] = df['preco_unitario'] * 1.10

# Converte a coluna de data para o tipo datetime (transformação 3)
df['data_venda'] = pd.to_datetime(df['data_venda'])

#  Extrai o mês da venda (transformação 4 - enriquecimento de dado)
df['mes_venda'] = df['data_venda'].dt.month

# Exporta o resultado para um novo CSV
df.to_csv('vendas_transformadas.csv', index=False)

print(" ETL executado com sucesso! Arquivo 'vendas_transformadas.csv' criado.")
