import pandas as pd
import openpyxl

# Carrega o arquivo Excel em um DataFrame
dataframe = pd.read_excel("02_03_04_vendas.xlsx")

# Imprime as primeiras linhas do DataFrame
print(dataframe.head())

# Amostra aleatória de 5 linhas do DataFrame
print(dataframe.sample(5))

# Verifica a quantidade de valores nulos em cada coluna
print(dataframe.isnull().sum())

# # Calcula a média da coluna "Vendas"
media = dataframe["Vendas"].mean()
print(media)

# Remove as linhas que possuem todos os valores nulos
dataframe.dropna(how="all", inplace=True)

# Calcula a coluna "Receita" multiplicando a coluna "Vendas" por ela mesma
dataframe["Receita"] = dataframe["Vendas"].mul(dataframe["Vendas"])

# Imprime as primeiras linhas do DataFrame com a coluna "Receita"
print(dataframe.head())

# Encontra o maior valor da coluna "Receita"
print("Maior receita: ", dataframe["Receita"].max())

# Obtém as 5 maiores receitas do DataFrame
print(dataframe.nlargest(5, "Receita"))

# Obtém as 5 menores receitas do DataFrame
print(dataframe.nsmallest(5, "Receita"))

# Agrupa os dados por cidade e calcula a soma da coluna "Receita" para cada cidade
print(dataframe.groupby("Cidade")["Receita"].sum())
