# **String Múltiplas Linhas**
---

As strings de múltiplas linhas em Python são usadas para representar strings que ocupam mais de uma linha de código. Essas strings podem ser definidas usando três aspas simples ou duplas.

~~~py
nome = """Meu nome é João
da Silva
e eu moro em São Paulo"""
print(nome)

Meu nome é João
da Silva
e eu moro em São Paulo
~~~

Nesse exemplo, a string nome é definida usando três aspas duplas para permitir que ela ocupe mais de uma linha de código. A string contém quebras de linha e é impressa no console usando a função print(). 

---
*Exemplo*

~~~py
print("""
========== MENU ==========
    1 - Sacar
    2 - Depositar
    3 - Sair
==========================
        Obrigado !!!
""")

#saida:
========== MENU ==========
    1 - Sacar
    2 - Depositar
    3 - Sair
==========================
        Obrigado !!!

~~~
---