# MongoDB x SQL

As principais diferenças entre o MongoDB e os bancos de dados relacionais SQL são:

Modelo de dados: 

O MongoDB é um banco de dados NoSQL orientado a documentos, enquanto os bancos de dados SQL são orientados a tabelas. Isso significa que o MongoDB armazena dados em documentos BSON, que podem conter vários campos com valores e tipos de dados diferentes. Já os bancos de dados SQL possuem tabelas com colunas bem definidas e estruturadas.

Flexibilidade:

 O MongoDB é mais flexível do que os bancos de dados SQL em relação ao esquema de dados. Em outras palavras, o MongoDB não exige que todas as entradas tenham a mesma estrutura, o que torna mais fácil e rápido adicionar ou modificar campos. Já nos bancos de dados SQL, mudanças no esquema podem ser mais complicadas e exigem que toda a tabela seja alterada.

Escalabilidade: 

O MongoDB é altamente escalável e pode ser facilmente dimensionado horizontalmente (adicionando mais servidores para distribuir a carga de trabalho). Já nos bancos de dados SQL, o escalonamento horizontal pode ser mais difícil e complexo devido às restrições do esquema e da integridade referencial.

Consultas: 

As consultas no MongoDB são realizadas usando uma linguagem de consulta de documentos e as operações são executadas em documentos individuais ou em grupos de documentos. Já as consultas SQL são feitas usando a linguagem de consulta SQL e geralmente são usadas para extrair dados de várias tabelas ao mesmo tempo.

Transações: 

Os bancos de dados SQL suportam transações ACID (Atomicidade, Consistência, Isolamento e Durabilidade), que garantem a integridade dos dados em caso de falhas ou conflitos. O MongoDB suporta transações em alguns cenários específicos, mas geralmente não tem o mesmo nível de segurança transacional que os bancos de dados SQL.

Geral: 

O MongoDB é mais adequado para aplicativos modernos que exigem flexibilidade, escalabilidade e desempenho em tempo real, enquanto os bancos de dados SQL são mais adequados para aplicativos que exigem transações ACID complexas e conformidade com padrões estritos de esquema de dados.

---

### Diferença de Código

* Exemplo de código em MongoDB:

~~~py
import pymongo

# conexão com o servidor MongoDB local
client = pymongo.MongoClient('mongodb://localhost:27017/')

# selecionando o banco de dados
db = client['exemplo_db']

# selecionando a coleção
col = db['exemplo_col']

# inserindo um documento na coleção
doc = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
col.insert_one(doc)

# buscando todos os documentos na coleção
for doc in col.find():
    print(doc)
~~~

Neste exemplo, estamos criando uma conexão com o servidor MongoDB local, selecionando um banco de dados e uma coleção, inserindo um documento na coleção e buscando todos os documentos na coleção.

* Exemplo de código em SQL:

~~~py
import sqlite3

# conexão com o banco de dados SQLite local
conn = sqlite3.connect('exemplo.db')

# criando uma tabela
conn.execute('CREATE TABLE IF NOT EXISTS exemplo_table (nome TEXT, idade INT, cidade TEXT)')

# inserindo um registro na tabela
conn.execute("INSERT INTO exemplo_table VALUES ('João', 30, 'São Paulo')")

# buscando todos os registros na tabela
cursor = conn.execute('SELECT * FROM exemplo_table')
for row in cursor:
    print(row)
~~~

Neste exemplo, estamos criando uma conexão com um banco de dados SQLite local, criando uma tabela, inserindo um registro na tabela e buscando todos os registros na tabela.

---