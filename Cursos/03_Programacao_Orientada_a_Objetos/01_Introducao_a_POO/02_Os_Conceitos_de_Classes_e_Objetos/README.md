# Os Conceitos de Classes e Objetos

Na programação orientada a objetos, uma classe é um modelo que define as propriedades e métodos (comportamentos) de um conjunto de objetos que possuem características semelhantes.

Por exemplo, uma classe "Carro" pode definir os atributos como marca, modelo, ano, cor, velocidade e métodos como acelerar, frear e ligar. Essa classe não é um objeto em si, mas sim uma descrição que pode ser usada para criar múltiplos objetos da mesma classe.

Já um objeto é uma instância específica de uma classe, que possui seus próprios valores para os atributos definidos pela classe e pode executar os métodos especificados. Por exemplo, se criarmos um objeto "MeuCarro" da classe "Carro", podemos definir que seu modelo é "Fusca" e sua cor é "Vermelho", além de executar os métodos como acelerar ou frear.

Em resumo, uma classe é um modelo para criar objetos que compartilham características e métodos comuns, enquanto um objeto é uma instância única dessa classe, que possui valores específicos para seus atributos e pode executar seus próprios métodos.


*Exemplo em código*
~~~py
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        
    def acelerar(self, incremento):
        self.velocidade += incremento
        
    def frear(self, decremento):
        if self.velocidade >= decremento:
            self.velocidade -= decremento
        else:
            self.velocidade = 0
            
    def ligar(self):
        print(f"O carro {self.modelo} da marca {self.marca} está ligado.")
        
meu_carro = Carro(marca="Fiat", modelo="Uno", ano=2015, cor="Azul")
print(meu_carro.modelo) # Imprime "Uno"
meu_carro.ligar() # Imprime "O carro Uno da marca Fiat está ligado."
meu_carro.acelerar(50) # Acelera 50 km/h
print(meu_carro.velocidade) # Imprime 50
meu_carro.frear(30) # Freia 30 km/h
print(meu_carro.velocidade) # Imprime 20
meu_carro.frear(25) # Freia 25 km/h
print(meu_carro.velocidade) # Imprime 0
~~~

Nesse exemplo, a classe "Carro" é definida com quatro atributos (marca, modelo, ano, cor) e três métodos (acelerar, frear e ligar). O método __init__ é um construtor que inicializa os atributos do objeto quando ele é criado. O método "acelerar" aumenta a velocidade do carro em um valor passado como parâmetro, enquanto o método "frear" reduz a velocidade do carro em um valor passado como parâmetro. O método "ligar" apenas imprime uma mensagem dizendo que o carro está ligado.

Em seguida, um objeto "meu_carro" é criado a partir da classe "Carro", com os valores passados como parâmetros. Em seguida, vários métodos são executados para modificar a velocidade do carro e imprimir os valores dos atributos.

---

