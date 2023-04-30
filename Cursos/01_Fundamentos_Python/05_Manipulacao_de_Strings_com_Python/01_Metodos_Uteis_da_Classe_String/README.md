# **Conhecendo Métodos Úteis da Classe String**
---
## **A Classe String**

A classe string em Python é uma sequência imutável de caracteres e é usada para manipular texto. A classe string oferece muitos métodos úteis para trabalhar com strings.

Além disso, a classe string suporta indexação e fatiamento, o que permite acessar e manipular partes específicas de uma string.


*  **Maiúscula, Minúscula e Título**

~~~py
curso = "pYtHon"

print(curso.upper())
>>> PYTHON

print(curso.lower())
>>> python

print(curso.title())
>>> Python
~~~

* **Eliminando Espaços em Branco**

~~~py
curso = "   Python"

print(curso.strip())
>>> "Python"

print(curso.lstrip())
>>> "Python "

print(curso.rstrip())
>>> "   Python"
~~~

* **Junção e Centralização**

~~~py
curso = "Python"

print(curso.center(10, "#"))
>>> "##Python##"

print(".".join(curso))
>>> "P.y.t.h.o.n"
~~~

---
