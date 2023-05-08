# Herança em POO

## O que é ?

Herança em Programação Orientada a Objetos (POO) é um conceito que permite criar novas classes a partir de classes já existentes. A classe original é chamada de classe base ou superclasse, enquanto a nova classe criada é chamada de classe derivada ou subclasse.

A subclasse herda todos os membros da classe base, incluindo seus atributos e métodos públicos e protegidos. A partir da subclasse, é possível adicionar novos atributos e métodos, ou modificar os já existentes. Além disso, a subclasse pode definir novos construtores e destrutores.

A herança é um dos pilares da POO e permite criar hierarquias de classes, onde as subclasses são cada vez mais especializadas do que as superclasses. Isso facilita a organização do código, a reutilização de classes e a manutenção do software.

~~~py
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def estudar(self):
        print(f"{self.nome} está estudando.")

# Exemplo de uso:

aluno = Aluno("João", 20, 12345)
aluno.falar() # Output: Olá, meu nome é João e tenho 20 anos.
aluno.estudar() # Output: João está estudando.
~~~

Nesse exemplo, a classe Aluno é uma subclasse de Pessoa, que é a superclasse. A subclasse herda os atributos nome e idade e o método falar da superclasse. A subclasse também adiciona um novo atributo matricula e um novo método estudar. A palavra-chave super() é usada para chamar o construtor da superclasse e inicializar seus atributos.

---

## Benefícios

* Reutilização de código:

 a herança permite que classes existentes sejam reutilizadas e estendidas em novas classes, evitando a necessidade de reescrever o mesmo código várias vezes.

* Redução de complexidade:

 a herança permite que hierarquias de classes sejam criadas, tornando o código mais fácil de ser organizado, mantido e entendido.

* Flexibilidade: 

a herança permite que as classes sejam estendidas e modificadas para atender às necessidades específicas de cada aplicação, sem precisar alterar a classe original.

* Polimorfismo:

 a herança permite que objetos de uma subclasse sejam tratados como objetos da superclasse, o que possibilita a criação de métodos genéricos que funcionam com objetos de várias classes diferentes.

* Abstração:

 a herança permite que as classes mais genéricas e abstratas sejam definidas em níveis mais altos da hierarquia, enquanto as classes mais específicas e detalhadas podem ser definidas em níveis mais baixos. Isso ajuda a separar as preocupações e a manter o código mais organizado.

Em resumo, a herança é uma técnica importante na POO que ajuda a melhorar a qualidade do código, a reduzir a redundância e a aumentar a flexibilidade do software.

---

## Herança Simples

A herança simples é quando uma classe herda de apenas uma classe pai. Ou seja, uma classe pode ter apenas uma classe pai, que é a superclasse. A herança simples é mais fácil de entender e é amplamente utilizada na POO.

---

## Herança Multipla

Já a herança múltipla é quando uma classe herda de duas ou mais classes pai. Isso significa que a subclasse terá acesso aos atributos e métodos de várias classes superiores. No entanto, a herança múltipla pode tornar o código mais complexo e difícil de entender, pois as classes podem ter atributos e métodos com o mesmo nome.

*OBS: Em algumas linguagens de programação, como Python, a herança múltipla é suportada, mas em outras, como Java, a herança múltipla não é permitida. Em vez disso, as classes podem implementar várias interfaces, que fornecem um conjunto de métodos que as classes devem implementar.*

---