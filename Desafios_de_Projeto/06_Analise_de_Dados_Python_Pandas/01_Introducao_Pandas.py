import pandas as pd

# Lendo o arquivo CSV
dataframe = pd.read_csv("01_countries_world.csv")

# Exibindo apenas as colunas desejadas
colunas_desejadas = ["Country", "Population"]
dataframe_desejado = dataframe[colunas_desejadas]

# Renomeando colunas
dataframe_desejado = dataframe_desejado.rename(columns={"Country": "Pais", "Population": "População"})

# Exibindo as 10 primeiras linhas do DataFrame com as colunas desejadas e renomeadas
print(dataframe_desejado.head(10))

# Exibindo o total de linhas e colunas com as colunas desejadas e renomeadas
print("Total de Linhas / Colunas: ", dataframe_desejado.shape)

# Exibindo as regiões únicas presentes na coluna "Region"
print(dataframe["Region"].unique())

# Agrupando por região e contando a quantidade de países únicos em cada região
country_count = dataframe.groupby("Region")["Country"].nunique()

# Exibindo a contagem de países únicos por região
print(country_count)