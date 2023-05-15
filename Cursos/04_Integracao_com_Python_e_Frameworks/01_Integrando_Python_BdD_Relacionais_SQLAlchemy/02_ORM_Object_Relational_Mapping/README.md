# Entendendo o modelo ORM – Object Relational Mapping

## ORM 

ORM (Object-Relational Mapping) é uma técnica de programação que permite que as aplicações se comuniquem com um banco de dados relacional usando objetos em vez de instruções SQL diretas.

Em um sistema que utiliza ORM, as tabelas do banco de dados são mapeadas para classes em um programa orientado a objetos, e as colunas do banco de dados são mapeadas para atributos das classes. As relações entre as tabelas são mapeadas para associações entre as classes. Dessa forma, é possível manipular dados do banco de dados por meio de objetos em um programa de maneira mais intuitiva e menos sujeita a erros.

Um exemplo de ORM popular é o framework Hibernate para Java, que mapeia objetos Java para tabelas do banco de dados relacional. Outros exemplos incluem o Entity Framework para .NET, o Django ORM para Python e o Ruby on Rails ActiveRecord para Ruby.

Embora o uso de ORM possa facilitar o desenvolvimento de aplicações, é importante lembrar que, em alguns casos, pode afetar o desempenho da aplicação. ORM pode gerar instruções SQL complexas e ineficientes que podem tornar as consultas ao banco de dados mais lentas. Por isso, é importante usar ORM com cuidado e considerar o desempenho ao projetar a aplicação.

---

## Vantagens e Desvantagens


#### Vantagens:

* Redução da complexidade do código:

 ORM pode reduzir a complexidade do código, pois permite que os desenvolvedores trabalhem com objetos em vez de lidar diretamente com o SQL.

* Facilidade de manutenção:

 ORM pode facilitar a manutenção da aplicação, pois as alterações no banco de dados podem ser feitas diretamente nas classes mapeadas, em vez de alterar diretamente as instruções SQL.

* Maior portabilidade:

 ORM pode tornar a aplicação mais portável, pois pode trabalhar com diferentes bancos de dados sem a necessidade de alterar o código.

* Melhor produtividade:

 ORM pode aumentar a produtividade dos desenvolvedores, pois reduz a quantidade de código que precisa ser escrito para acessar o banco de dados.

#### Desvantagens:

* Overhead de desempenho:

 ORM pode ter um overhead de desempenho, pois as instruções SQL geradas pelo ORM podem ser menos eficientes do que as instruções SQL escritas manualmente.

* Complexidade de configuração:

 ORM pode ser complexo de configurar, especialmente em grandes aplicações, e pode exigir uma curva de aprendizado para os desenvolvedores.

* Limitações do mapeamento objeto-relacional:

 ORM pode ter limitações no mapeamento objeto-relacional, especialmente quando se trabalha com modelos de dados mais complexos ou com bancos de dados legados.

* Dificuldade de depuração:

 ORM pode tornar a depuração mais difícil, pois as instruções SQL geradas pelo ORM podem ser difíceis de serem rastreadas.

Em resumo, ORM pode oferecer muitas vantagens na programação de aplicações, mas também pode apresentar desafios e limitações. A escolha de usar ORM deve ser considerada cuidadosamente, dependendo das necessidades da aplicação e das habilidades dos desenvolvedores.

---

## Entidade

Em bancos de dados, uma entidade é um objeto ou conceito do mundo real que é representado em uma tabela. Cada entidade é representada por uma tabela com colunas que correspondem às propriedades ou atributos da entidade. Por exemplo, uma tabela "clientes" pode representar a entidade de um cliente, com colunas para o nome, endereço, telefone e outras informações relevantes. As entidades são geralmente identificadas por uma chave primária, que é um valor único que permite a identificação de cada registro na tabela. As entidades são um dos principais componentes do modelo de dados relacional e são usadas para organizar e armazenar informações em um banco de dados.

---

## Porque utilizar ORM ?

Usar ORM pode trazer muitos benefícios para uma aplicação, incluindo simplificação do código, aumento da produtividade, portabilidade, facilidade de manutenção, segurança e testabilidade. No entanto, é importante lembrar que o uso de ORM pode afetar o desempenho da aplicação e pode exigir um esforço adicional de configuração e aprendizado.

---
