# **Interpolação de Variáveis**
---

A interpolação de variáveis em Python é uma maneira de inserir valores de variáveis dentro de uma string, usando uma sintaxe especial que usa chaves {} para indicar onde as variáveis devem ser inseridas, e o método format() para formatar a string.

* **Old Style "%"**

O % na interpolação de variáveis em Python é uma sintaxe antiga que ainda é suportada, mas não é recomendada, e consiste em usar %s para indicar onde as variáveis devem ser inseridas dentro de uma string e, em seguida, usar o operador % para especificar as variáveis a serem interpoladas.

~~~py
nome = "João"
idade = 25
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))
~~~

* **Método "format"**

O método format() em Python é uma maneira de inserir valores de variáveis dentro de uma string, usando uma sintaxe especial que usa chaves {} para indicar onde as variáveis devem ser inseridas. O método format() pode ser usado para formatar strings de várias maneiras, como especificar a largura e precisão de números, o número de casas decimais para valores de ponto flutuante e a justificação do texto. Ele pode ser usado com uma ou mais variáveis e aceita argumentos nomeados ou posicionais.

~~~py
nome = "João"
idade = 25
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
~~~

* **"f-string"**

O f-string em Python é uma forma mais recente e conveniente de interpolar variáveis em uma string, introduzida na versão 3.6 do Python. Ele usa uma sintaxe especial com prefixo f e chaves {} para indicar onde as variáveis devem ser inseridas. O f-string também permite a execução de expressões Python dentro das chaves.

~~~py
nome = "João"
idade = 25
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

preco = 9.99
quantidade = 2
total = preco * quantidade
print(f"O preço total é R${total:.2f}.")
#.2f dentro das chaves indica que o valor de ponto flutuante deve ser formatado com duas casas decimais
~~~

---