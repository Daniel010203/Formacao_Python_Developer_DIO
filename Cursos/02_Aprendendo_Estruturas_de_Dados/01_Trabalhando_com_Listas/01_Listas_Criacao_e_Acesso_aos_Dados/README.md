# **Listas: Criação e Acesso aos Dados**
---

## **Criando Listas**


Em Python, uma lista é uma estrutura de dados que pode armazenar uma coleção ordenada de elementos. As listas são criadas usando colchetes, e os elementos da lista são separados por vírgulas. As listas podem conter elementos de diferentes tipos de dados, incluindo strings, números e outras listas. Você também pode adicionar, remover e modificar elementos em uma lista após a criação.

~~~py
frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
~~~

---

## **Acesso Direto**

Em Python, é possível acessar um elemento específico de uma lista usando o conceito de "acesso direto", que significa acessar um elemento pelo seu índice, que é sua posição na lista. Os índices de uma lista começam em 0 para o primeiro elemento e vão até n-1 para o último elemento, onde n é o número total de elementos na lista.

~~~py
frutas = ["laranja", "maca", "uva"]
frutas[0] # maca
frutas[2] # uva
~~~

---

## **Índicas Negativos**

Em Python, é possível acessar os elementos de uma lista usando índices negativos. Quando você usa um índice negativo, o Python começa a contar a partir do final da lista. Ou seja, o índice -1 representa o último elemento da lista, o índice -2 representa o penúltimo elemento, e assim por diante.

~~~py
frutas = ["laranja", "maca", "uva", "pera"]
frutas[-1] # pera
frutas[-3] # maca
~~~

---

## **Listas Aninhadas**

Em Python, você pode criar uma lista aninhada, que é uma lista que contém outras listas como elementos. Essa estrutura de dados é útil quando você precisa representar dados hierárquicos ou tabelas.

~~~py
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0]       # [1. "a", 2]
matriz[0][0]    # 1
matriz[0][-1]   # 2
matriz[0-1]     # "c"
~~~

---

## **Fatiamento**

O fatiamento (slicing, em inglês) é uma operação que permite obter uma parte de uma sequência (uma lista, uma string, uma tupla, etc.) a partir de um intervalo de índices.

~~~py
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]       # ["t","h", "o", "n"]
lista[:2]       # ["p", "y"]
lista[1:3]      # ["y", "t"]
lista[0:3:2]    # ["p", "t"]
lista[::]       # ["p", "y", "t", "h", "o", "n"]
lista[::-1]     # ["n", "o", "h", "t", "y", "p"]
~~~

---

## **Iterar Listas**

Iterar listas em Python significa percorrer todos os seus elementos um a um para realizar alguma ação ou operação sobre cada um deles. Isso pode ser feito de várias maneiras, como por exemplo usando o loop for, o método map, ou usando compreensão de listas. A escolha da abordagem depende do contexto específico e do que se deseja fazer com os elementos da lista.

~~~py
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
~~~

---

## **Função Enumerate**

A função enumerate em Python permite iterar sobre uma lista (ou qualquer objeto iterável) ao mesmo tempo em que mantém um contador automático que acompanha o índice de cada elemento da lista.

~~~py

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
~~~

---

## **Compreensão de Listas**

Compreensão de lista é uma construção da linguagem Python que permite criar listas de forma concisa e expressiva a partir de uma sequência existente ou objeto iterável, aplicando uma expressão a cada elemento e/ou filtrando elementos indesejados com uma condição if.

* **Filtro 1**

~~~py
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
~~~

* **Filtro 2**

~~~py
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
~~~

* **Modificando Valores Versão 1**

~~~py
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    quadrado.append(numero ** 2)
~~~


* **Modificando Valores Versão 2**

~~~py
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
~~~

---