# O que é Pymongo?

* Módulo para MongoDB
* Autor: MongoDB Python Team
* Apache Software License
* Formato: BSON
* Intereção com documentos
* Coleções e demais recursos do MongoDB
* Suporte MongoDB (3.6, 4.0, 4.2, 4.4 e 5.0)

Pymongo é um módulo Python que fornece uma API para interagir com bancos de dados MongoDB. Com o Pymongo, podemos realizar diversas operações em bancos de dados MongoDB, como inserir, atualizar, excluir e consultar documentos, além de gerenciar índices, autenticação e replicação. É amplamente utilizado para desenvolver aplicativos web, IoT, análise de dados, aprendizado de máquina e outras aplicações em Python que precisam armazenar dados em um banco de dados não relacional.

---

## Como instalar 

Para instalar o Pymongo usando pip, basta abrir o terminal ou prompt de comando e digitar o seguinte comando:

~~~cmd
pip install pymongo
~~~

Esse comando irá baixar e instalar o Pymongo e suas dependências. Certifique-se de ter o pip instalado em sua máquina antes de executar esse comando. Se não tiver, você pode instalá-lo através do comando python -m ensurepip --default-pip (no Windows) ou sudo apt-get install python3-pip (no Linux).

---
*Exemplo de Código*

~~~py
import pymongo

# Conectar ao servidor MongoDB local
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Selecionar o banco de dados "mydatabase"
db = client['mydatabase']

# Criar uma coleção chamada "customers"
col = db['customers']

# Inserir um documento na coleção
doc = {'name': 'John', 'address': 'Highway 37'}
x = col.insert_one(doc)
print(x.inserted_id)

# Inserir múltiplos documentos na coleção
docs = [
  {'name': 'Amy', 'address': 'Apple st 652'},
  {'name': 'Hannah', 'address': 'Mountain 21'},
  {'name': 'Michael', 'address': 'Valley 345'},
  {'name': 'Sandy', 'address': 'Ocean blvd 2'},
  {'name': 'Betty', 'address': 'Green Grass 1'},
  {'name': 'Richard', 'address': 'Sky st 331'},
  {'name': 'Susan', 'address': 'One way 98'},
  {'name': 'Vicky', 'address': 'Yellow Garden 2'},
  {'name': 'Ben', 'address': 'Park Lane 38'},
  {'name': 'William', 'address': 'Central st 954'},
  {'name': 'Chuck', 'address': 'Main Road 989'},
  {'name': 'Viola', 'address': 'Sideway 1633'}
]
x = col.insert_many(docs)
print(x.inserted_ids)

# Buscar um documento da coleção
x = col.find_one()
print(x)

# Buscar todos os documentos da coleção
for x in col.find():
  print(x)

# Buscar documentos com critérios específicos
query = {'address': 'Park Lane 38'}
x = col.find_one(query)
print(x)

query = {'address': {'$regex': '^S'}}
for x in col.find(query):
  print(x)

# Ordenar documentos
query = {'name': 1}
for x in col.find().sort(query):
  print(x)

# Atualizar documentos
query = {'address': 'Mountain 21'}
new_values = {'$set': {'address': 'Valley 345'}}
x = col.update_one(query, new_values)
print(x.modified_count)

query = {'address': {'$regex': '^S'}}
new_values = {'$set': {'name': 'Minnie'}}
x = col.update_many(query, new_values)
print(x.modified_count)

# Deletar documentos
query = {'address': 'Mountain 21'}
x = col.delete_one(query)
print(x.deleted_count)

query = {'address': {'$regex': '^S'}}
x = col.delete_many(query)
print(x.deleted_count)

# Deletar a coleção
x = col.drop()
print(x)
~~~

Neste exemplo, primeiro conectamos ao servidor MongoDB local e selecionamos o banco de dados "mydatabase". Depois, criamos uma coleção chamada "customers" e inserimos alguns documentos nela, buscamos documentos, ordenamos documentos, atualizamos documentos e excluímos documentos. Por fim, excluímos a coleção.

---