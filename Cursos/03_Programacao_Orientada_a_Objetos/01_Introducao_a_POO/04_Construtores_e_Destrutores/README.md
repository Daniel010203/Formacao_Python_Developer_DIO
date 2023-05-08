# Contrutores e Destrutores
---

## Método Contrutor 

Em Python, o método construtor é um método especial chamado:

~~~py
__init__()
~~~

que é executado automaticamente quando um objeto é criado a partir de uma classe. O objetivo desse método é inicializar os atributos do objeto com valores específicos.

A sintaxe básica para definir um construtor em uma classe Python é a seguinte:

~~~py
class MinhaClasse:
    def __init__(self, parametro1, parametro2, ...):
        self.atributo1 = parametro1
        self.atributo2 = parametro2
        ...
~~~

Nesse exemplo, MinhaClasse é o nome da classe, e __init__ é o nome do método construtor. O parâmetro self é obrigatório e representa o objeto sendo criado. Os parâmetros parametro1, parametro2, etc. são opcionais e representam os valores que serão atribuídos aos atributos do objeto.

Dentro do método __init__, cada atributo do objeto é inicializado com um valor específico usando a sintaxe self.nome_atributo = valor. Por exemplo:

~~~py
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
~~~

Nesse exemplo, a classe Pessoa tem dois atributos (nome e idade). O método __init__ recebe dois parâmetros (nome e idade) e inicializa os atributos correspondentes com os valores passados como parâmetros.

Ao criar um objeto a partir da classe Pessoa, o construtor __init__ é automaticamente chamado com os valores dos parâmetros passados, como mostrado no exemplo abaixo:

~~~py
pessoa1 = Pessoa("João", 30)
print(pessoa1.nome)  # Imprime "João"
print(pessoa1.idade)  # Imprime 30
~~~

Dessa forma, o construtor permite que os objetos de uma classe sejam inicializados com valores específicos em seus atributos.

---

## Método Destrutor

Em Python, o método destrutor é um método especial chamado:

~~~py
__del__()
~~~

que é executado automaticamente quando um objeto é destruído, ou seja, quando ele não é mais utilizado pelo programa. O objetivo desse método é realizar operações de limpeza antes que o objeto seja removido da memória.

A sintaxe básica para definir um destrutor em uma classe Python é a seguinte:

~~~py
class MinhaClasse:
    def __del__(self):
        # Código de limpeza aqui
~~~

Nesse exemplo, MinhaClasse é o nome da classe, e __del__ é o nome do método destrutor. O parâmetro self é obrigatório e representa o objeto sendo destruído.

Dentro do método __del__, pode-se colocar qualquer código de limpeza que seja necessário antes que o objeto seja removido da memória. Isso pode incluir, por exemplo, fechar arquivos abertos, liberar recursos do sistema, ou enviar uma mensagem de log.

É importante lembrar que o momento exato em que o método destrutor é chamado não é determinístico em Python, já que depende da política de gerenciamento de memória do interpretador. Em geral, o método destrutor é chamado quando o objeto não está mais sendo usado pelo programa, mas não há garantias sobre quando isso irá ocorrer.

Por esse motivo, é recomendável que o método destrutor seja usado apenas em situações em que seja realmente necessário realizar operações de limpeza antes que o objeto seja removido da memória. Em muitos casos, é possível evitar o uso do método destrutor e deixar que o interpretador do Python faça a gestão automática da memória, utilizando o coletor de lixo do Python.

---