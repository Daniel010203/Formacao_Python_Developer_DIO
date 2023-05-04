# **Dominando Funções Python - Parte 01**
---

Em Python, uma função é um bloco de código que executa uma tarefa específica e pode ser chamado de outros lugares do programa. Aqui estão algumas coisas importantes a serem lembradas sobre funções em Python:

Sintaxe: uma função é definida com a palavra-chave def, seguida do nome da função e, opcionalmente, de parâmetros entre parênteses. O corpo da função é definido por indentação.

~~~py
def minha_funcao(param1, param2):
    # corpo da função aqui
~~~

Parâmetros: uma função pode receber zero ou mais parâmetros. Os parâmetros são variáveis ​​que contêm valores que a função pode usar.

~~~py
def soma(x, y):
    return x + y
~~~

Retorno: uma função pode retornar um valor usando a palavra-chave return. O valor retornado pode ser qualquer tipo de objeto Python.

~~~py
def soma(x, y):
    return x + y

resultado = soma(2, 3)
print(resultado) # saída: 5
~~~

Escopo: variáveis ​​definidas dentro de uma função são locais para essa função e não são acessíveis fora dela. Variáveis ​​definidas fora de uma função são globais e podem ser acessadas de qualquer lugar do programa.

~~~py
def minha_funcao():
    x = 10 # x é uma variável local para a função
    print(x)

x = 5 # x é uma variável global
minha_funcao() # saída: 10
print(x) # saída: 5
~~~

Docstrings: uma função pode ter uma string de documentação, conhecida como docstring, que descreve o que a função faz e quais parâmetros ela espera. A docstring é definida como a primeira coisa na definição da função e é delimitada por três aspas.

~~~py
def minha_funcao(param1, param2):
    """
    Esta é uma função de exemplo que recebe dois parâmetros e retorna uma string.
    """
    # corpo da função aqui
~~~

Essas são apenas algumas das coisas importantes a serem lembradas sobre funções em Python. As funções são uma parte fundamental da programação em Python e são usadas para dividir o código em partes menores e mais gerenciáveis, tornando o código mais legível e reutilizável.

---

## *args e **kwargs

*args e **kwargs são dois recursos muito úteis em Python quando se trabalha com funções que têm um número variável de argumentos.

*args

 permite que você passe um número variável de argumentos posicionais para a função. Os argumentos são empacotados em uma tupla dentro da função e podem ser acessados ​​como qualquer outra tupla.

~~~py
def minha_funcao(*args):
    for arg in args:
        print(arg)

minha_funcao(1, 2, 3) # saída: 1, 2, 3
minha_funcao('a', 'b', 'c', 'd') # saída: 'a', 'b', 'c', 'd'
~~~

**kwargs

 permite que você passe um número variável de argumentos nomeados para a função. Os argumentos são empacotados em um dicionário dentro da função e podem ser acessados ​​como qualquer outro dicionário.

 ~~~py
 def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')

minha_funcao(nome='João', idade=25) # saída: nome = João, idade = 25
minha_funcao(cidade='São Paulo', país='Brasil', idioma='Português') # saída: cidade = São Paulo, país = Brasil, idioma = Português
~~~

Além disso, é possível usar tanto *args quanto **kwargs na mesma função para receber argumentos posicionais e nomeados variáveis.

~~~py
def minha_funcao(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')

minha_funcao(1, 2, 3, nome='João', idade=25) # saída: 1, 2, 3, nome = João, idade = 25
minha_funcao('a', 'b', cidade='São Paulo', país='Brasil') # saída: 'a', 'b', cidade = São Paulo, país = Brasil
~~~

OBS *args e **kwargs são muito úteis quando você precisa lidar com funções que aceitam um número variável de argumentos.

---