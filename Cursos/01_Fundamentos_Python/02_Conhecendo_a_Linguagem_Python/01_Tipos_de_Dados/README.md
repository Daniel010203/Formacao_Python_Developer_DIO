## Conhecendo a Linguagem de Programação Python

*Documentação de estudos - **Ariel Riello***

---

### **Tipos de Dados**

---

**Built-in**

Em Python, existem diversos tipos de dados "built-in" ou integrados na linguagem, que estão disponíveis por padrão e não requerem a importação de nenhuma biblioteca adicional. Alguns dos principais tipos de dados "built-in" em Python incluem:

---


**Tipos Númericos**

* **Inteiros (int):**
    *  representam números inteiros, positivos ou negativos, sem casas decimais. Eles podem ser usados para realizar operações aritméticas, como adição, subtração, multiplicação e divisão inteira.

* **Números de ponto flutuante (float):**
    * representam números com casas decimais. Eles podem ser usados para realizar operações aritméticas que envolvem números reais, como divisão com resultado fracionário.

* **Complexos (complex):**
    * representam números complexos, com uma parte real e uma parte imaginária. Eles podem ser usados para realizar operações matemáticas em que aparecem números complexos, como na teoria dos circuitos elétricos.

---


**Tipos de Texto**

* **Strings (str):**
    * representam texto ou cadeias de caracteres. Elas podem ser usadas para armazenar e manipular texto, como nomes de pessoas, endereços de e-mail e outras informações textuais.

---

**Tipos de Sequência**

* **Listas (list):**
    *  representam coleções ordenadas e mutáveis de valores. Elas podem ser usadas para armazenar uma sequência de valores e permitir que sejam adicionados, removidos e modificados.

* **Tuplas (tuple):**
    * representam coleções ordenadas e imutáveis de valores. Elas podem ser usadas para armazenar uma sequência de valores que não podem ser modificados após a criação da tupla.

* **Range (range):**
    * representam uma sequência imutável de números inteiros. Elas podem ser usadas para gerar sequências de números inteiros de forma eficiente.

* **Bytes (bytes):**
    * representam sequências de bytes. Elas podem ser usadas para armazenar dados binários, como arquivos de imagem ou de áudio.

* **Bytearrays (bytearray):**
    * representam sequências mutáveis de bytes. Elas podem ser usadas para armazenar e modificar dados binários de forma eficiente.

---

**Tipos de Mapeamento**

* **Dicionários (dict):**
    * representam coleções não ordenadas de pares chave-valor. Eles podem ser usados para armazenar e recuperar informações associadas a uma determinada chave.

---

**Tipos de Conjunto**

* **Conjuntos (set):**
    * representam coleções não ordenadas e sem elementos duplicados. Eles podem ser usados para armazenar um conjunto de valores e realizar operações matemáticas com conjuntos, como união, interseção e diferença.

* **Frozensets (frozenset):**
    * representam conjuntos imutáveis. Eles são semelhantes aos conjuntos, mas não permitem que os elementos sejam adicionados, removidos ou modificados após a criação do frozenset.

---

**Tipos especiais**

* **Booleanos (bool):**
    * é um tipo de dado que pode representar dois valores: True ou False. Esses valores são usados para expressar afirmações lógicas verdadeiras ou falsas. Eles são comumente usados em estruturas de controle de fluxo, como em condicionais e loops, para tomar decisões com base em expressões booleanas.

* **NoneType (None):**
    * representam um valor nulo ou vazio. Eles são usados para indicar que uma variável não possui nenhum valor atribuído.

---

OBS: *Lembre-se de que alguns tipos de dados pertencem a várias categorias. Por exemplo, as strings são tipos de texto, mas também podem ser consideradas sequências de caracteres. Os conjuntos e dicionários são tipos de mapeamento, mas também podem ser considerados tipos de conjunto e sequência, respectivamente.*

---

*Codigos feitos em aula:*

~~~Python
print(11 + 10 + 1000)
print(1.5 + 0.5)
print(True)
print(False)
print("Python")

int()
float()
str()
bool()
~~~