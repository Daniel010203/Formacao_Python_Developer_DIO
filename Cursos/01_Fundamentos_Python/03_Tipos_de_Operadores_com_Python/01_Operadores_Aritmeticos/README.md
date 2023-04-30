# **01 - Operadores Aritméticos**


Os operadores aritméticos em Python são usados para executar operações matemáticas em valores numéricos. Abaixo está uma lista dos operadores aritméticos em Python:

* Adição (+): 
    * Soma dois valores numéricos.

* Subtração (-): 
    * Subtrai o segundo valor numérico do primeiro.

* Multiplicação (*): 
    * Multiplica dois valores numéricos.

* Divisão (/): 
    * Divide o primeiro valor numérico pelo segundo.

* Divisão inteira (//): 
    * Retorna a parte inteira do resultado da divisão.

* Resto (%) : 
    * Retorna o resto da divisão inteira entre dois valores numéricos.

* Exponenciação (**): 
    * Eleva o primeiro valor numérico à potência do segundo.

~~~py
x = 10
y = 3

soma = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y
divisao_inteira = x // y
resto = x % y
exponenciacao = x ** y

print(soma, subtracao, multiplicacao, divisao, divisao_inteira, resto, exponenciacao)
~~~

O resultado da execução deste código será:  **13 7 30 3.3333333333333335 3 1 1000**


Observe que a divisão de 10 por 3 resulta em um número com parte decimal. Isso ocorre porque estamos usando a divisão normal (/). Se quisermos obter a divisão inteira, podemos usar o operador // em vez disso.

---

*Códigos feitos em aula:*

~~~py
produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4
print(x
)
y = (10 / 2) + (25 * 2) - (2 ** 2)
print(y)
~~~

---