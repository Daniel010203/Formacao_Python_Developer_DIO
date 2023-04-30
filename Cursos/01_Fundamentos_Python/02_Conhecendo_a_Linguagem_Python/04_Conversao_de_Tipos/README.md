## Conhecendo a Linguagem de Programação Python

*Documentação de estudos - **Ariel Riello***

---

### **Conversão de Tipos**

---

A conversão de tipo em Python é a transformação de um valor de um tipo de dado em outro tipo de dado. Existem diversas funções nativas em Python que permitem realizar essa conversão, que pode ser necessária em várias situações, como para realizar operações matemáticas ou manipular strings.

Aqui estão alguns exemplos de como realizar a conversão de tipo em Python:

1. Conversão de string para int ou float:

~~~Python
numero_int = int("10") # Converte a string "10" em um número inteiro
numero_float = float("10.5") # Converte a string "10.5" em um número de ponto flutuante
~~~

2. Conversão de int ou float para string:

~~~Python
numero_int_string = str(10) # Converte o número inteiro 10 em uma string "10"
numero_float_string = str(10.5) # Converte o número de ponto flutuante 10.5 em uma string "10.5"
~~~

3. Conversão de string para lista:

~~~Python
lista = list("Python") # Converte a string "Python" em uma lista ["P", "y", "t", "h", "o", "n"]
~~~

4. Conversão de lista para string:

~~~Python
texto = "".join(["P", "y", "t", "h", "o", "n"]) # Converte a lista ["P", "y", "t", "h", "o", "n"] em uma string "Python"
~~~

5. Conversão de int para bool:

~~~Python
bool_int = bool(0) # Converte o número inteiro 0 em False
~~~

6. Conversão de bool para int:

~~~Python
int_bool = int(True) # Converte o booleano True em 1
~~~

OBS: *É importante lembrar que nem todas as conversões são possíveis em Python. Por exemplo, não é possível converter uma string que não representa um número para um número inteiro ou de ponto flutuante. É sempre importante verificar se a conversão é possível e se o resultado é coerente com o que se espera.*

---