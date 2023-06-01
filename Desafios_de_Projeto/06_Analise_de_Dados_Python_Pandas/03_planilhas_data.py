import pandas as pd
import openpyxl

# Importar o arquivo Excel como um dataframe usando a biblioteca pandas
dataframe = pd.read_excel("02_03_04_vendas.xlsx")

# Converter a coluna "Data" para o formato de string com o formato "%Y%m%d" e, em seguida, para o tipo de dado Int64
dataframe["Data"] = dataframe["Data"].dt.strftime("%Y%m%d").astype("Int64")

# Imprimir os tipos de dados das colunas do dataframe
print(dataframe.dtypes)

# Converter a coluna "Data" de volta para o tipo de dado datetime
dataframe["Data"] = pd.to_datetime(dataframe["Data"])

# Imprimir os tipos de dados das colunas do dataframe novamente
print(dataframe.dtypes)

# Agrupar o dataframe pela coluna "Data" (ano) e calcular a soma da coluna "Quantidade" para cada ano
dataframe_quantidade_data = dataframe.groupby(dataframe["Data"].dt.year)["Quantidade"].sum()

# Imprimir as primeiras linhas do dataframe resultante
print(dataframe_quantidade_data.head())

# Adicionar uma nova coluna "Ano" ao dataframe, contendo o ano extraído da coluna "Data"
dataframe["Ano"] = dataframe["Data"].dt.year

# Imprimir uma amostra aleatória de 10 linhas do dataframe
print(dataframe.sample(10))

# Imprimir o valor mínimo da coluna "Ano"
print(dataframe["Ano"].min())
