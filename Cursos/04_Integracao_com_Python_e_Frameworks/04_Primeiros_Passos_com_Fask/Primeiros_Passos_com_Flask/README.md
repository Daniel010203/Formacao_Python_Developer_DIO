# Flask Framework

Flask é um microframework para desenvolvimento web em Python. Ele é projetado para ser leve e simples de usar, permitindo que os desenvolvedores criem aplicativos web rapidamente e com menos sobrecarga.

O Flask oferece apenas o básico necessário para criar aplicativos web, sem muitos recursos adicionais. Ele não inclui uma camada de abstração de banco de dados, nem um mecanismo de autenticação incorporado, por exemplo. No entanto, é fácil estender o Flask com bibliotecas e pacotes adicionais para adicionar funcionalidades específicas ao aplicativo.

O Flask usa o padrão de roteamento baseado em função, permitindo que as funções Python sejam mapeadas para URLs específicos em um aplicativo. Ele também suporta a criação de APIs RESTful e o uso de templates para a geração de conteúdo HTML dinâmico.

No geral, o Flask é uma ótima escolha para desenvolvedores que desejam criar aplicativos web simples e eficientes em Python sem muita complexidade ou sobrecarga de recursos.

---

## Flask-SQLAlchemy

Flask-SQLAlchemy é uma extensão do Flask que fornece integração com o SQLAlchemy, um ORM (Object-Relational Mapping) para Python.

O SQLAlchemy é uma biblioteca que fornece uma camada de abstração de banco de dados que permite que os desenvolvedores trabalhem com banco de dados relacionais usando objetos Python. Ele permite que os desenvolvedores escrevam consultas em Python e abstrai as diferenças entre diferentes bancos de dados, tornando o código mais portável.

Com o Flask-SQLAlchemy, os desenvolvedores podem integrar facilmente o SQLAlchemy em um aplicativo Flask. Ele fornece uma maneira fácil de configurar a conexão do banco de dados, criar modelos para representar as tabelas do banco de dados e executar consultas usando o SQLAlchemy. Além disso, o Flask-SQLAlchemy fornece suporte para migrações de banco de dados, o que torna a atualização do banco de dados muito mais fácil.

Em resumo, o Flask-SQLAlchemy é uma extensão útil para o Flask que permite que os desenvolvedores trabalhem com bancos de dados relacionais usando o SQLAlchemy de maneira fácil e eficiente.

Exemplo básico de como utilizar o Flask-SQLAlchemy em uma aplicação Flask:

~~~py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def index():
    user = User(name='John')
    db.session.add(user)
    db.session.commit()
    return 'User added to the database!'

if __name__ == '__main__':
    app.run()
~~~

---

## Como definir um objeto Flask-SQLAlchemy para um banco de dados

Para definir um objeto Flask-SQLAlchemy para um banco de dados, é preciso criar uma classe que herda de db.Model. Essa classe representa uma tabela no banco de dados e define seus campos e relacionamentos com outras tabelas.

Aqui está um exemplo básico de como definir um objeto Flask-SQLAlchemy para um banco de dados SQLite:

~~~py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
~~~

Neste exemplo, estamos criando uma classe User que herda de db.Model do Flask-SQLAlchemy. A classe define três campos: id, name, email e password, que são representados como colunas na tabela users do banco de dados. O campo id é definido como chave primária da tabela.

É importante definir o nome da tabela com o atributo __tablename__. Isso garante que o nome da tabela seja consistente com o restante do código.

Após definir a classe, é preciso inicializar o objeto db do Flask-SQLAlchemy, que representa a conexão com o banco de dados, e associar a classe User ao objeto db. Isso é geralmente feito em um arquivo separado que é importado em outras partes do código da aplicação Flask.


~~~py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

from models import User  # Importa a classe User definida anteriormente

# Resto do código da aplicação Flask
~~~

Neste exemplo, estamos criando um objeto Flask-SQLAlchemy chamado db e associando-o à aplicação Flask. Estamos também importando a classe User definida anteriormente em outro arquivo chamado models.py.

Dessa forma, podemos usar a classe User em outras partes do código da aplicação Flask para fazer consultas e modificações no banco de dados.

---