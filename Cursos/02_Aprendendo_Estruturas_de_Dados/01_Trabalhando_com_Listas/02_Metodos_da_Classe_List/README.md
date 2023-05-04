# **Métodos da Classe LIST**
---

**[].append**

Adiciona um elemento ao final da lista.

~~~py
lista = [1, 2, 3]
lista.append(4)
print(lista)  # output: [1, 2, 3, 4]
~~~

---

**[].clear**

Remove todos os elementos da lista. 

~~~py
lista = [1, 2, 3]
lista.clear()
print(lista)  # output: []
~~~

---

**[].copy**

Retorna uma cópia da lista.

~~~py
lista = [1, 2, 3]
lista2 = lista.copy()
lista2.append(4)
print(lista)   # output: [1, 2, 3]
print(lista2)  # output: [1, 2, 3, 4]
~~~

---

**[].count**

Retorna a quantidade de ocorrências de um determinado elemento na lista. 

~~~py
lista = [1, 2, 3, 2, 4, 2]
count_2 = lista.count(2)
print(count_2)  # output: 3
~~~

---

**[].extend**

Adiciona os elementos de outra lista ao final da lista atual. 

~~~py
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)  # output: [1, 2, 3, 4, 5, 6]

~~~

---

**[].index**

Retorna o índice da primeira ocorrência de um elemento na lista.

~~~py
lista = [1, 2, 3, 2, 4, 2]
index_2 = lista.index(2)
print(index_2)  # output: 1

~~~
---

**[].pop**

Remove e retorna o elemento no índice especificado (ou o último elemento, se nenhum índice for especificado).

~~~py
lista = [1, 2, 3]
elemento_removido = lista.pop(1)
print(elemento_removido)  # output: 2
print(lista)             # output: [1, 3]
~~~
---

**[].remove**

Remove a primeira ocorrência de um elemento da lista. 

~~~py
lista = [1, 2, 3, 2, 4, 2]
lista.remove(2)
print(lista)  # output: [1, 3, 2, 4, 2]
~~~

---

**[].reverse**

Inverte a ordem dos elementos na lista. 

~~~py
lista = [1, 2, 3]
lista.reverse()
print(lista)  # output: [3, 2, 1]
~~~

---

**[].sort**

Ordena os elementos da lista em ordem crescente (ou em ordem decrescente, se especificado o parâmetro reverse=True). 

~~~py
lista = [3, 1, 2]
lista.sort()
print(lista)  # output: [1, 2, 3]
~~~

---

**len**

A função len() em Python é usada para retornar o número de elementos em uma sequência, como uma lista, tupla, conjunto, dicionário ou string. O exemplo a seguir demonstra como usar a função len() para obter o tamanho de uma lista:

~~~py
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5
~~~

---

**sorted**

A função sorted() em Python é usada para ordenar uma sequência, como uma lista, tupla, conjunto, dicionário ou string. O exemplo a seguir demonstra como usar a função sorted() para classificar uma lista em ordem crescente:

~~~py
my_list = [3, 2, 1, 5, 4]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 2, 3, 4, 5]
~~~

Observe que a função sorted() retorna uma nova lista ordenada e não altera a lista original.

---