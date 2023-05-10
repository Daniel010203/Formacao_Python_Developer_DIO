# Propriedades - property()

Em Python, uma property é uma forma de definir um método de acesso e/ou alteração de um atributo de classe como se fosse um atributo comum, mas com a possibilidade de adicionar lógica de validação ou cálculo a essas operações.

Uma property é criada usando a função property(), que recebe como argumentos os métodos getter, setter e deleter, respectivamente, e retorna um objeto property. O método getter é chamado quando se tenta acessar o valor da propriedade, o setter quando se tenta atribuir um valor a ela, e o deleter quando se usa a palavra-chave del para apagar a propriedade.

Por exemplo, suponha que você tenha uma classe Pessoa com os atributos nome e idade, mas que queira garantir que a idade nunca seja negativa. Você pode definir uma property idade que inclua essa verificação:

~~~py
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa")
        self._idade = valor
~~~

Com essa definição, o atributo _idade é considerado privado (por convenção, usa-se o prefixo _ para indicar que um atributo é privado em Python), mas a propriedade idade pode ser usada como se fosse um atributo comum:

~~~py
p = Pessoa("João", 25)
print(p.idade)  # 25
p.idade = 30
print(p.idade)  # 30
p.idade = -10  # gera um ValueError
~~~

---