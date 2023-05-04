## **Conjuntos**

Em Python, os conjuntos são uma estrutura de dados que armazenam uma coleção de elementos únicos e não ordenados. Aqui estão alguns exemplos de como criar e usar conjuntos em Python:

Criando um conjunto:

~~~py
# Criando um conjunto:

conjunto = {1, 2, 3, 4, 5}

# Adicionando elementos ao conjunto:

conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto) # saída: {1, 2, 3, 4}

# Removendo elementos do conjunto:

conjunto = {1, 2, 3, 4}
conjunto.remove(3)
print(conjunto) # saída: {1, 2, 4}

# Verificando se um elemento pertence ao conjunto:

conjunto = {1, 2, 3, 4}
if 3 in conjunto:
    print("O conjunto contém o número 3")
else:
    print("O conjunto não contém o número 3")

# Unindo dois conjuntos:

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)
print(uniao) # saída: {1, 2, 3, 4, 5}


# Encontrando a interseção de dois conjuntos:

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
intersecao = conjunto1.intersection(conjunto2)
print(intersecao) # saída: {3}

# Verificando se dois conjuntos são disjuntos:

conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
if conjunto1.isdisjoint(conjunto2):
    print("Os conjuntos são disjuntos")
else:
    print("Os conjuntos não são disjuntos")


# Verificando se um conjunto é subconjunto de outro conjunto:

conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}
if conjunto1.issubset(conjunto2):
    print("O conjunto1 é um subconjunto do conjunto2")
else:
    print("O conjunto1 não é um subconjunto do conjunto2")

~~~

Os conjuntos em Python são úteis para muitas tarefas, como remoção de duplicatas, verificação de pertinência, união e interseção de conjuntos e muito mais.

---
## **SET**

Em Python, o tipo set é uma variação do tipo conjunto. Os sets são muito semelhantes aos conjuntos, mas com uma diferença importante: os conjuntos são mutáveis, enquanto os sets são imutáveis. Isso significa que, uma vez criado um set, ele não pode ser modificado. 

Criando um set:

~~~py
meu_set = {1, 2, 3}

# ou

meu_set = set([1, 2, 3])
~~~

---

Aqui estão alguns dos métodos mais comuns da classe set em Python:

* add(x): 
    * adiciona o elemento x ao set.

* clear(): 
    * remove todos os elementos do set.

* copy(): 
    * retorna uma cópia do set.

* difference(*others): 
    * retorna um novo set com todos os elementos que estão no set, mas não em others.

* discard(x):
    * remove o elemento x do set, se estiver presente.

* intersection(*others):
    * retorna um novo set com todos os elementos que estão em ambos os sets.

* isdisjoint(other):
    * retorna True se o set não tiver elementos em comum com other.

* issubset(other):
    * retorna True se todos os elementos do set estiverem em other.

* issuperset(other):
    * retorna True se todos os elementos de other estiverem no set.

* pop():
    * remove e retorna um elemento aleatório do set.

* remove(x):
    * remove o elemento x do set, gerando um erro se ele não estiver presente.

* symmetric_difference(other):
    * retorna um novo set com todos os elementos que estão em um dos sets, mas não em ambos.

* union(*others):
    * retorna um novo set com todos os elementos de todos os sets.

Esses são apenas alguns dos métodos disponíveis na classe set. Para ver a lista completa de métodos, você pode consultar a documentação oficial do Python.

---