## **Dominando Funções em Python - Parte 02**
---

## Parametros Especiais

Em Python, existem alguns parâmetros especiais que podem ser usados em funções. Além dos parâmetros posicionais e nomeados regulares, que são aqueles que você passa quando chama a função, há os seguintes parâmetros especiais:

Parâmetros padrão: são valores padrão que você pode atribuir a um parâmetro da função, caso nenhum valor seja passado para esse parâmetro durante a chamada da função. Por exemplo:

~~~py
def minha_funcao(a, b=10):
    print(a, b)

minha_funcao(5) # saída: 5, 10
minha_funcao(5, 20) # saída: 5, 20
~~~

Parâmetros arbitrários: são parâmetros que permitem que você passe um número variável de argumentos para a função. Existem dois tipos de parâmetros arbitrários: *args e **kwargs. Veja a Parte 01 para mais detalhes.

Parâmetro de desempacotamento: é um parâmetro que permite que você passe uma lista ou tupla de argumentos para uma função e desempacote esses argumentos para parâmetros separados da função. Para fazer isso, basta colocar um asterisco antes do nome do parâmetro. Por exemplo:

~~~py
def minha_funcao(a, b, c):
    print(a, b, c)

minha_lista = [1, 2, 3]

minha_funcao(*minha_lista) # saída: 1, 2, 3
~~~

Parâmetro de palavra-chave: é um parâmetro que permite que você passe argumentos nomeados para uma função e crie um dicionário dentro da função com esses argumentos. Para fazer isso, basta colocar dois asteriscos antes do nome do parâmetro. Por exemplo:

~~~py
def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

minha_funcao(nome='João', idade=25) # saída: nome João, idade 25
~~~

Parâmetro de argumentos posicionais apenas: é um parâmetro que só aceita argumentos posicionais e não aceita argumentos nomeados. Para fazer isso, basta colocar um asterisco antes do nome do parâmetro, mas sem nomeá-lo. Por exemplo:

~~~py
def minha_funcao(*, a, b):
    print(a, b)

minha_funcao(a=1, b=2) # saída: 1, 2
minha_funcao(1, 2) # erro: TypeError: minha_funcao() takes 0 positional arguments but 2 were given
~~~

---

## **Objetos de Primeira Classe**

Em Python, as funções são consideradas objetos de primeira classe, o que significa que elas podem ser tratadas como qualquer outro objeto. Isso permite que você faça coisas como:

* Atribuir funções a variáveis.
* Passar funções como argumentos para outras funções.
* Retornar funções de outras funções.

Por exemplo, aqui está uma função que retorna uma outra função:

~~~py
def criar_funcao(multiplicador):
    def funcao_interna(numero):
        return numero * multiplicador
    return funcao_interna

dobro = criar_funcao(2)
triplo = criar_funcao(3)

print(dobro(5)) # saída: 10
print(triplo(5)) # saída: 15
~~~

A função criar_funcao retorna uma outra função (funcao_interna), que é definida dentro dela. Quando chamamos criar_funcao(2), ela retorna uma função que multiplica um número por 2. Essa função é armazenada na variável dobro. Em seguida, podemos chamar dobro(5) para obter o resultado de 5 multiplicado por 2, que é 10.

Da mesma forma, chamando criar_funcao(3) retorna uma função que multiplica um número por 3, que é armazenada na variável triplo. Em seguida, chamamos triplo(5) para obter o resultado de 5 multiplicado por 3, que é 15.

Isso é apenas um exemplo simples, mas mostra como as funções podem ser tratadas como objetos de primeira classe em Python. Isso é útil para criar funções genéricas que podem ser personalizadas de acordo com a necessidade do usuário.

---