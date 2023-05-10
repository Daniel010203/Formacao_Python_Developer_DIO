# Classes Abstratas - Biblioteca ABC

A biblioteca ABC (Abstract Base Classes) em Python é uma ferramenta para implementar interfaces abstratas. Uma interface abstrata é um conjunto de métodos que uma classe deve implementar para satisfazer a interface. As classes que implementam a interface abstrata podem ter diferentes implementações para esses métodos, mas eles devem fornecer uma implementação para cada método definido na interface abstrata.

Usando a biblioteca ABC, podemos definir classes abstratas que servem como modelos para outras classes. Uma classe abstrata é uma classe que não pode ser instanciada e deve ser subclassificada para ser usada. As subclasses devem implementar todos os métodos abstratos definidos na classe abstrata.

Por exemplo, podemos criar uma interface abstrata "Veiculo" que define os métodos "acelerar", "frear" e "virar". Qualquer classe que implemente essa interface deve fornecer implementações para esses três métodos. A seguir, podemos definir uma classe "Carro" que herda a interface "Veiculo" e fornece suas próprias implementações para os métodos "acelerar", "frear" e "virar".

~~~py
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frear(self):
        pass
    
    @abstractmethod
    def virar(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando...")
    
    def frear(self):
        print("Carro freando...")
    
    def virar(self):
        print("Carro virando...")
~~~

Observe que a classe "Veiculo" é uma classe abstrata e define os métodos "acelerar", "frear" e "virar" como métodos abstratos. Isso significa que qualquer classe que herde de "Veiculo" deve implementar esses três métodos. A classe "Carro" herda a interface "Veiculo" e fornece suas próprias implementações para os três métodos abstratos.

---