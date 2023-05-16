# Treinamento a PEP 8 - IDENTACAO

# ------------------------------ COMENTARIOS e DOCSTRINGS ----------------------------- #

# Comentarios
# Sempre comecar com leitra miuscuala
# Comentarios de uma linha

# Docstring
"""
    isso é uma docstring
"""
'''
    isso tambem é uma doc string
'''
# Objetivo documentar o obejtivo de algo (codigo inteiro (top do codigo),
#  funcao (dentro da funcao), metodo (dentro do metodo), classe (dentro da classe))

# Exemplo

def set_name(self, name):
    """
        Esse metodo tem por objetivo setar o nome do objeto instanciado
    pela classe.

    :param name: O nome definido pelo usuario
    :return: Retorna um nome via print
    """
    self.name = name
    print("O nome é: ", name)
    return self.name

# ------------------------------ IMPORTACOES ----------------------------- #

# Errado
import pandas, matplotlib

# Correto
import pandas
import matplotlib

# Quebra de linha para multiplos imports
from pandas import (
    read_csv,
    Series,
    DataFrame,
    HDFStore,
)

# Ordem de imports
import sys  # Nativos primeiro do python
from pandas import array  # modulo especifico
from caminho import exemplo  # do proprio projeto

# ------------------------------ VARIAVEIS ----------------------------- #

# Usar underline para separar os nomes das variaveis
def print_hi(name):
    pass

# variaveis sempre em minusculo

variavel = 0  # Dois espaços para comentarios ao lado (no minimo)

# sempre usar o padrao de espaçamentos
# Errado
x =1
y=2
#Correto
x = 1
y = 2

# Constantes (sempre tudo maiusculo (uppercase))
CONSTANTE = 100

lista = [1,2,3,4,5,6,7,8,9]  # Errado (espacamento e disposicao)

matriz = [  # Certo
    1, 2, 3
    4, 5, 6
    7, 8, 9
]

# ------------------------------ CLASSES ----------------------------- #

class PessoaJuridica:  # Nao separa o nome de uma casse com underline (Camel Case)
    # Nome das classes sempre com letra maiusculo
    def __init__(self, message):
        self.inicio = message
    # Sempre começar com self (semelhante ao "this")

# Dois espaços em branco após a classe

# ------------------------------ FUNCOES ----------------------------- #

 # Nome das funções sempre intuitivos
def media_aluno(nota_1, nota_2, nota_3): 
    return nota_1 + nota_2 + nota_3 / 3

# Errado
def retorno_funcao_args(arg_one, arg_two, arg_three, arg_four):
    pass

# Quebra de linha em parametros muito logos

# Correto
def retorno_funcao_args(arg_one, arg_two,
                        arg_three, arg_four):
    pass

# ------------------------------ TAB e ESPAÇO ----------------------------- #

# TAB pode variar de configuração de computador para computador, então foi definido usar a 
# configuracao de 4 espaços para a tabulacao

# Testamdo o codigo para erro de interpretacao de tabulacao
# python2 -t code.py

# ------------------------------ ATALHOS VS CODE ----------------------------- #

# "Shift" + "Alt" + "F" = Formata todo codigo

# ------------------------------ ESPACAMENTO ----------------------------- #

def media_aluno(nota1, nota2, divisor):
    total = (nota1+nota2)/divisor
    # dois espacamentos entre a funcao e o restante do codigo

    media_aluno(5,9,2)  # Errado
    media_aluno(2, 3, 2)  # Certo

funcao_ficticia(vetor[1,2,3],{'key':2})  # Errado
funcao_ficticia(vetor[1, 2, 3],{'key': 2})  # Certo

if x==4: print (x,y); x,y=y,x  # Errado

if x == 4:  # Certo
    print(x, y)
    x, y = y, x

# Tuplas
foo = (0,)  # Certo
bar=(0, )  # Errado

# ------------------------------ -//- ----------------------------- #