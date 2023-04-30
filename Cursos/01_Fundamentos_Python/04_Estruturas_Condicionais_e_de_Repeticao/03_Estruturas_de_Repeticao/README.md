# **Estruturas de Repetição**
---

Em Python, as estruturas de repetição são usadas para executar um bloco de código várias vezes. Existem duas principais estruturas de repetição em Python: o loop while e o loop for.

---

## **Loop "while"**
O loop while é usado para executar um bloco de código enquanto uma condição for verdadeira. 

A sintaxe básica do loop while em Python é a seguinte:

~~~py
while condição:
    # bloco de código a ser executado enquanto a condição for verdadeira
~~~

Veja um exemplo de loop while:

~~~py
i = 1
while i <= 10:
    print(i)
    i += 1
~~~

Neste exemplo, o loop while é usado para imprimir os números de 1 a 10. A variável i é inicializada com o valor 1. O loop while é executado enquanto i for menor ou igual a 10. Em cada iteração do loop, o valor atual de i é impresso na tela e i é incrementado em 1.

---

## **Loop "for"**
O loop for é usado para executar um bloco de código para cada item em uma sequência. 

A sintaxe básica do loop for em Python é a seguinte:

~~~py
for item in sequência:
    # bloco de código a ser executado para cada item na sequência
~~~

Veja um exemplo de loop for:

~~~py
for i in range(1, 11):
    print(i)
~~~

Neste exemplo, o loop for é usado para imprimir os números de 1 a 10. A função range(1, 11) retorna uma sequência de números de 1 a 10. O loop for é executado para cada número na sequência, e o valor atual de i é impresso na tela em cada iteração.

O Python também tem outras funções que retornam sequências, como list, tuple e string, que podem ser usadas no loop for para executar um bloco de código para cada item na sequência.

Em ambos os loops while e for, é importante usar a lógica adequada para garantir que o loop não se torne infinito ou interrompa prematuramente. Lembre-se de que a indentação também é muito importante em Python ao escrever loops, e o bloco de código dentro do loop deve estar indentado corretamente.

---