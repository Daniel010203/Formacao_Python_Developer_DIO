# **Indentação e blocos**

## **Indentação**

A identação em Python é a maneira de definir a estrutura de blocos de código em um programa. Em vez de usar chaves ou palavras-chave de fim de bloco como em outras linguagens de programação, o Python usa a indentação para determinar onde um bloco começa e termina.

A indentação é feita usando espaços em branco ou tabulações e é importante garantir que ela esteja correta, pois a indentação incorreta pode levar a erros de sintaxe ou semântica no código.

Por exemplo, em um bloco de código como um loop ou uma função, o código dentro do bloco deve ser indentado com um número consistente de espaços ou tabulações para que o Python entenda que é parte do mesmo bloco.

Exemplo:

~~~py
for i in range(10):
    if i % 2 == 0:
        print(i, "é um número par")
    else:
        print(i, "é um número ímpar")
~~~

Observe que o código dentro do loop "for" e dentro do "if" está indentado com um nível de espaço adicional para indicar que é parte do bloco.

---

## **Bloco**

Em Python, um bloco de código é um conjunto de instruções que são executadas juntas como uma unidade. Os blocos são definidos pela indentação, que é a quantidade de espaços em branco no início de cada linha de código. A indentação é usada para agrupar as instruções que pertencem a um determinado bloco.

Os blocos são usados em várias estruturas de controle de fluxo, como condicionais (if, elif, else) e loops (for, while). Em um bloco condicional, as instruções dentro do bloco if são executadas se a condição for verdadeira, e as instruções dentro do bloco else são executadas se a condição for falsa. No caso do bloco elif, se a condição if for falsa e a condição elif for verdadeira, as instruções dentro do bloco elif são executadas.

Veja um exemplo de bloco em um condicional:

~~~py
x = 10
if x > 5:
    print("x é maior do que 5")
else:
    print("x é menor ou igual a 5")
~~~

Neste exemplo, o bloco if contém a instrução print("x é maior do que 5"), que é executada porque a condição x > 5 é verdadeira. O bloco else contém a instrução print("x é menor ou igual a 5"), que não é executada neste caso.

Em um loop, as instruções dentro do bloco são repetidas várias vezes até que a condição do loop seja falsa. Veja um exemplo de bloco em um loop:

~~~py
for i in range(5):
    print(i)
~~~

Neste exemplo, o bloco contém a instrução print(i), que é executada cinco vezes, uma vez para cada valor de i no intervalo de 0 a 4.

Lembre-se de que a indentação é muito importante em Python, já que define a estrutura do seu código. Se a indentação estiver incorreta, você pode encontrar erros de sintaxe. Portanto, sempre verifique se a indentação está correta ao escrever seu código.

---