# **Conhecendo Tuplas em Python**
---

Em Python, uma tupla é uma sequência imutável de objetos. Em outras palavras, uma vez criada, uma tupla não pode ser modificada. As tuplas são definidas usando parênteses () e os elementos são separados por vírgulas. 

~~~py
tupla = (1, 2, "três")
~~~

Aqui está um exemplo de código que ilustra como criar e acessar elementos de uma tupla:

~~~py
# criando uma tupla
tupla = (1, 2, 3, 4, 5)

# acessando elementos da tupla
print(tupla[0])  # saída: 1
print(tupla[2])  # saída: 3
~~~

Uma das principais diferenças entre as tuplas e as listas em Python é que as listas são mutáveis, enquanto as tuplas são imutáveis. Isso significa que você pode alterar os elementos de uma lista, mas não pode alterar os elementos de uma tupla. Por exemplo:

~~~py
# exemplo de lista mutável
lista = [1, 2, 3]
lista[1] = 4
print(lista)  # saída: [1, 4, 3]

# exemplo de tupla imutável
tupla = (1, 2, 3)
tupla[1] = 4  # Erro! As tuplas são imutáveis.
~~~

Outra diferença importante entre as tuplas e as listas é que as tuplas geralmente têm um desempenho melhor em termos de velocidade e uso de memória. Isso ocorre porque as tuplas são imutáveis, o que significa que o Python não precisa alocar e desalocar memória para elas conforme elas são modificadas.

---

## **Métodos Tuplas**

Em Python, as tuplas são imutáveis e possuem métodos que permitem acessar e manipular seus elementos. Aqui estão alguns dos métodos mais comuns das tuplas, com exemplos de código:

* count(): 

Este método retorna o número de vezes que um determinado elemento aparece na tupla.

~~~py
tupla = (1, 2, 3, 4, 2, 2)
index_2 = tupla.index(2)
print(index_2)  # saída: 1
~~~

* index(): 

Este método retorna o índice da primeira ocorrência de um determinado elemento na tupla.

~~~py
tupla = (1, 2, 3, 4, 2, 2)
index_2 = tupla.index(2)
print(index_2)  # saída: 1
~~~

* len(): 

Este método retorna o número de elementos na tupla.

~~~py
tupla = (1, 2, 3, 4, 5)
tam_tupla = len(tupla)
print(tam_tupla)  # saída: 5
~~~

* sorted():

 Este método retorna uma nova lista ordenada dos elementos da tupla.

~~~py
tupla = (3, 2, 1, 5, 4)
lista_ordenada = sorted(tupla)
print(lista_ordenada)  # saída: [1, 2, 3, 4, 5]
~~~

* max(): 

Este método retorna o valor máximo na tupla.

~~~py
tupla = (3, 2, 1, 5, 4)
valor_maximo = max(tupla)
print(valor_maximo)  # saída: 5
~~~

* min():

Este método retorna o valor mínimo na tupla.

~~~py
tupla = (3, 2, 1, 5, 4)
valor_minimo = min(tupla)
print(valor_minimo)  # saída: 1
~~~

*OBS: É importante lembrar que, como as tuplas são imutáveis, todos os métodos acima retornam uma nova tupla ou uma lista, em vez de modificar a tupla original.*

---