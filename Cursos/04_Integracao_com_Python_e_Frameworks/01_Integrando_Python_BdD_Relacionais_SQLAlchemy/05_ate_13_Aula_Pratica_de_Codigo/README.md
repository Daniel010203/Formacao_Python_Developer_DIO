# Aulas 05 até 13

* Criando as entidades com declarative_base – Parte 1

* Criando as entidades com declarative_base – Parte 2

* Definindo os Relacionamentos e Método de Representação

* Considerações sobre o código

* Conectando ao SQLite utilizando Engines e Inspecionamento o SQlite

* Criando uma Sessão para Persistir dados no SQlite

* Executando consultas ao BD – SQLAlchemy ORM

* Executando consultas com ORDER BY, JOIN Statement e Função COUNT

---

## Explicando o Código feito em aula

Este código é um exemplo de como usar a biblioteca SQLAlchemy em Python para criar um banco de dados relacional e fazer operações básicas de CRUD (Create, Read, Update, Delete).

A primeira seção do código importa os módulos necessários da SQLAlchemy. Em seguida, é definida a classe User, que representa uma tabela no banco de dados e possui colunas para os atributos id, name, fullname, e address. A classe Address também é definida para representar outra tabela no banco de dados, com colunas para id, email_address, e user_id. As classes são definidas usando a sintaxe de mapeamento de objeto-relacional (ORM) da SQLAlchemy, que mapeia as classes Python para tabelas do banco de dados.

Depois disso, é criado um objeto engine para conectar e interagir com o banco de dados, usando o SQLite como exemplo. Em seguida, é invocado o método create_all do objeto metadata para criar as tabelas no banco de dados. A partir daí, é usada uma sessão para interagir com o banco de dados, que é aberta com o comando with Session(engine) as session:.

No restante do código, exemplos de operações básicas de CRUD são demonstrados usando a sessão SQLAlchemy para recuperar informações de usuários e endereços de e-mail de usuários, ordenar e contar instâncias da classe User, e fazer uma junção entre as tabelas User e Address. Os resultados dessas operações são impressos na saída padrão.

---