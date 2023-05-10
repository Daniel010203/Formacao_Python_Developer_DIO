# O que são Interfaces

Em programação, uma interface é um tipo abstrato de dados que define um conjunto de métodos ou operações que uma classe deve implementar para ser considerada compatível com essa interface. Em outras palavras, é um contrato que define o comportamento esperado de uma classe.

Uma interface não contém implementações de métodos, apenas suas assinaturas, ou seja, os nomes dos métodos, seus parâmetros e seus tipos de retorno. Cada classe que implementa uma interface deve implementar todos os métodos definidos nessa interface.

O uso de interfaces ajuda a garantir que as classes sejam interoperáveis e possam ser usadas de maneira genérica, sem depender de detalhes de implementação específicos da classe. As interfaces também ajudam a promover o princípio de abstração, que permite aos desenvolvedores se concentrarem nos conceitos e comportamentos importantes de uma classe em vez de se preocupar com detalhes de implementação irrelevantes.

Em Python, a linguagem não possui uma declaração explícita de interface, mas o conceito pode ser implementado por meio de classes abstratas, que definem métodos sem implementação. Uma classe que herda de uma classe abstrata deve implementar todos os métodos abstratos da classe mãe para ser considerada compatível com essa interface.

---