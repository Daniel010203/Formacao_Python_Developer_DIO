# **Estruturas Condicionais**

Em Python, as estruturas condicionais permitem que você execute um bloco de código se uma condição for verdadeira e outro bloco de código se a condição for falsa. Existem três tipos principais de estruturas condicionais em Python: if, if-else e if-elif-else.

---

## **IF**

A estrutura if é usada para executar um bloco de código se uma condição for verdadeira. Veja um exemplo:

~~~py
idade = 18
if idade >= 18:
    print("Você é maior de idade")
~~~

Neste exemplo, a condição idade >= 18 é verdadeira, então a instrução dentro do bloco if é executada, imprimindo "Você é maior de idade".

---

## **IF-ELSE**

A estrutura if-else é usada para executar um bloco de código se a condição for verdadeira e outro bloco de código se a condição for falsa. Veja um exemplo:

~~~py
idade = 16
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
~~~

Neste exemplo, a condição idade >= 18 é falsa, então a instrução dentro do bloco else é executada, imprimindo "Você é menor de idade".

---

## **IF-ELIF-ELSE**

A estrutura if-elif-else é usada quando há várias condições a serem testadas. O bloco if é testado primeiro, seguido de zero ou mais blocos elif e, finalmente, um bloco else, que é executado se todas as condições anteriores forem falsas. Veja um exemplo:

~~~py
nota = 8
if nota >= 9:
    print("Você tirou nota A")
elif nota >= 7:
    print("Você tirou nota B")
elif nota >= 5:
    print("Você tirou nota C")
else:
    print("Você tirou nota D ou F")
~~~

Neste exemplo, a condição nota >= 9 é falsa, então o bloco elif é testado. A condição nota >= 7 é verdadeira, então a instrução dentro desse bloco é executada, imprimindo "Você tirou nota B".

Lembre-se de que a indentação é muito importante em Python ao escrever estruturas condicionais. Todas as instruções dentro de um bloco devem ter a mesma indentação.

---

## **IF Aninhado**

O if aninhado em Python é uma estrutura condicional que permite testar várias condições encadeando vários blocos if-else dentro de outros. O if aninhado é útil quando você precisa testar várias condições e executar um bloco de código diferente para cada condição.

Veja um exemplo de if aninhado:

~~~py
idade = 18
if idade >= 18:
    if idade == 18:
        print("Você acabou de atingir a maioridade")
    else:
        print("Você é maior de idade há mais tempo")
else:
    print("Você é menor de idade")
~~~

Neste exemplo, o primeiro bloco if testa se a idade é maior ou igual a 18. Se essa condição for verdadeira, o segundo bloco if é testado para verificar se a idade é igual a 18. Se a segunda condição for verdadeira, a instrução dentro do segundo bloco if é executada, imprimindo "Você acabou de atingir a maioridade". Caso contrário, a instrução dentro do else do primeiro bloco if é executada, imprimindo "Você é maior de idade há mais tempo".

Se a condição do primeiro bloco if for falsa, a instrução dentro do else é executada, imprimindo "Você é menor de idade".

---

## **IF Ternário**

O if ternário em Python é uma forma simplificada de escrever uma instrução condicional em apenas uma linha de código. Ele permite testar uma condição e executar uma instrução diferente com base no resultado do teste. O if ternário é escrito em uma única linha usando a sintaxe expressão_verdadeira if condição else expressão_falsa.

Veja um exemplo de if ternário:

~~~py
idade = 18
maioridade = True if idade >= 18 else False
print(maioridade)
~~~

Neste exemplo, o if ternário é usado para testar se a idade é maior ou igual a 18. Se a condição for verdadeira, a variável maioridade é definida como True. Caso contrário, a variável maioridade é definida como False. Em seguida, a instrução print(maioridade) é usada para imprimir o valor da variável maioridade.

Note que o if ternário é uma forma compacta e eficiente de escrever uma instrução condicional em uma única linha de código, mas pode ser menos legível do que escrever a instrução condicional completa com if-else em várias linhas.

---