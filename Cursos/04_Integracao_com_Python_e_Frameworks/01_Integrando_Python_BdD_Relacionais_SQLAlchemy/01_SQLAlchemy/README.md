# Explorando a biblioteca SQLAlchemy

## SQLAlchemy

* Framework - open source
* Licença MIT - 2009
* Mapeamento Objeto Relacional
* Vastamento utilizado
* Framework completo
* Flexibilização do SQL
* Segurança nas instruçoes


O SQLAlchemy é uma biblioteca de mapeamento objeto-relacional (ORM) em Python, que permite interagir com bancos de dados relacionais usando objetos Python. Ele suporta vários bancos de dados, incluindo PostgreSQL, MySQL e SQLite, e oferece uma ampla gama de recursos, incluindo geração de esquemas de banco de dados, criação e consulta de objetos, suporte a transações e muito mais. O SQLAlchemy também é altamente personalizável e pode ser estendido com plug-ins personalizados para atender às necessidades específicas do projeto.

---

## Dialetos

O SQLAlchemy suporta uma variedade de dialetos, que são adaptadores de banco de dados específicos que permitem que a biblioteca se comunique com diferentes bancos de dados. Alguns dos dialetos suportados pelo SQLAlchemy incluem:

* SQLite
* PostgreSQL
* MySQL
* Oracle
* Microsoft SQL Server

Cada dialeto fornece suporte para as peculiaridades e recursos específicos do banco de dados que ele representa, permitindo que os usuários do SQLAlchemy aproveitem ao máximo as capacidades de seus sistemas de banco de dados subjacentes. Além disso, o SQLAlchemy fornece um dialeto genérico que pode ser usado para se comunicar com bancos de dados SQL padrão, mas com funcionalidades mais limitadas.

---

## Recursos

O SQLAlchemy oferece uma ampla variedade de recursos para trabalhar com bancos de dados relacionais em Python. Alguns dos principais recursos incluem:

* ORM:

 O SQLAlchemy oferece um mapeamento objeto-relacional completo, permitindo que os desenvolvedores interajam com bancos de dados relacionais usando objetos Python. Isso permite que os desenvolvedores trabalhem com bancos de dados de uma forma mais natural e intuitiva, sem precisar se preocupar com a escrita de instruções SQL.

* Expressões SQL:

 O SQLAlchemy oferece uma linguagem de expressão SQL em Python, permitindo que os desenvolvedores gerem instruções SQL de forma programática. Isso torna mais fácil a criação de instruções SQL complexas e dinâmicas.

* Geração de esquemas:

 O SQLAlchemy permite a geração automática de esquemas de banco de dados a partir de classes Python, facilitando a criação e manutenção de bancos de dados.

* Transações:

 O SQLAlchemy oferece suporte a transações, permitindo que as operações de banco de dados sejam agrupadas em transações atômicas e seguras.

* Pooling de conexão:

 O SQLAlchemy oferece pooling de conexão, permitindo que várias conexões ao banco de dados sejam compartilhadas entre as requisições, melhorando o desempenho e a escalabilidade.

Suporte a vários bancos de dados: O SQLAlchemy suporta uma ampla variedade de bancos de dados, incluindo PostgreSQL, MySQL, SQLite, Oracle e Microsoft SQL Server, entre outros.

---

## Extensões

O SQLAlchemy também oferece uma série de extensões que podem ser adicionadas à biblioteca para fornecer recursos adicionais ou facilitar a integração com outras tecnologias. Algumas das extensões mais populares incluem:

* *lask-SQLAlchemy:

 Uma extensão para o framework web Flask, que fornece integração fácil entre o SQLAlchemy e o Flask.

* Alembic:

 Uma ferramenta de migração de banco de dados que trabalha em conjunto com o SQLAlchemy, permitindo a migração de esquemas de banco de dados de forma eficiente e controlada.

* GeoAlchemy:

 Uma extensão do SQLAlchemy que fornece suporte a tipos de dados geoespaciais, como pontos, linhas e polígonos.

* SQLAlchemy-Searchable:

 Uma extensão que adiciona recursos de pesquisa aprimorados ao SQLAlchemy, permitindo que os desenvolvedores pesquisem o banco de dados usando texto completo ou busca avançada.

* SQLAlchemy-Continuum:

 Uma extensão que adiciona recursos de controle de versão aprimorados ao SQLAlchemy, permitindo que os desenvolvedores rastreiem e gerenciem alterações no banco de dados ao longo do tempo.

* SQLAlchemy-Utils:

 Uma biblioteca de utilitários que estende o SQLAlchemy com recursos adicionais, como validação de dados, geração de senhas seguras e cálculo de estatísticas de banco de dados.

 ---

 *Exemplo de Código*

 ~~~py
 from sqlalchemy import Column, JSON, Integer
 from sqlalchemy.ext.declarative import declarative_base
 from sqlalchemy.ext.indexable import index_property

 Base = declarative_base()

 class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    data = Column(JSON)

    name = index_property('data', 'name')
~~~

Este código utiliza a biblioteca SQLAlchemy para definir uma classe chamada "Person" que mapeia um objeto Python para uma tabela chamada "person" em um banco de dados relacional.

A classe Person possui três atributos: "id", "data" e "name". O atributo "id" é uma chave primária que é um objeto do tipo inteiro (Integer). O atributo "data" é do tipo JSON e contém um dicionário Python com informações sobre a pessoa.

O atributo "name" é uma propriedade de índice (index_property) que utiliza a chave "name" dentro do dicionário do atributo "data" para indexar a tabela do banco de dados, tornando mais eficiente a busca por nomes.

O código também importa as classes Column e Integer do SQLAlchemy, que são utilizadas para definir o tipo dos atributos da classe Person, e a classe declarative_base, que é usada como base para definir as classes de mapeamento objeto-relacional.

---