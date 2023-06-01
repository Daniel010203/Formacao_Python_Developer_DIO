import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

# Carregar o arquivo Excel como um dataframe usando a biblioteca pandas
dataframe = pd.read_excel("02_03_04_vendas.xlsx")

# Contar o número de ocorrências de cada valor na coluna "ID"
total_id = dataframe["ID"].value_counts(ascending=False)

# Imprimir o total de lojas registradas
print("Total de Lojas Registradas:", total_id)

# Criar um gráfico de barras para a coluna "Vendas"
dataframe["Vendas"].plot.barh()

# Criar um gráfico de pizza para o total de vendas por loja
dataframe.groupby(dataframe["Loja"])["Vendas"].sum().plot.pie()

# Criar um gráfico de barras para o total de ocorrências de cada loja
dataframe["Loja"].value_counts().plot.bar(title="Total de Lojas", color="red")
plt.xlabel("Quantidade")
plt.ylabel("Lojas")

# Exibir o gráfico
plt.show()

# Você pode ir treinado usando varios comandos da biblioteca pandas e matplotlib
# Conferir documentasão nos sites: https://pandas.pydata.org /  https://matplotlib.org