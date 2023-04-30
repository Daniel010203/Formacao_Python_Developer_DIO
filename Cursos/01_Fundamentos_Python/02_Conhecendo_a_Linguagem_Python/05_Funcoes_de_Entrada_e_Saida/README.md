## Conhecendo a Linguagem de Programação Python

*Documentação de estudos - **Ariel Riello***

---

### **Funções de Entrada e Saida**

---

Em Python, existem funções nativas que permitem realizar operações de entrada e saída de dados. Essas operações são muito importantes em muitos programas, já que permitem a interação com o usuário, a leitura de dados de arquivos, entre outras funcionalidades.

Aqui estão alguns exemplos das funções de entrada e saída mais comuns em Python:

1. Função "input()" para receber entrada do usuário:

~~~Python
nome = input("Digite seu nome: ")
print("Seu nome é", nome)
~~~

2. Função "print()" para imprimir saída na tela:

~~~Python
nome = "João"
print("Olá, meu nome é", nome)
~~~

3. Funções "format()" e "f-string" para formatar a saída:

~~~Python
nome = "João"
idade = 30
print("Meu nome é {} e eu tenho {} anos".format(nome, idade))

# ou com f-string
print(f"Meu nome é {nome} e eu tenho {idade} anos")
~~~


OBS: *Essas são apenas algumas das muitas funções de entrada e saída disponíveis em Python. É importante ler a documentação oficial e pesquisar sobre outras funções disponíveis para saber como utilizá-las corretamente.*

---

**END e SEP**

Em Python, end e sep são dois parâmetros opcionais da função print(), que permitem personalizar o comportamento da função de saída de texto.

O parâmetro end permite definir o que será impresso ao final de cada chamada da função print(). Por padrão, o valor de end é uma quebra de linha, ou seja, após a impressão da mensagem, o cursor é movido para a próxima linha. Mas é possível mudar esse comportamento, como no exemplo abaixo:

~~~Python
print("Olá", end=", ")
print("mundo!")
~~~

Neste caso, o resultado será:

~~~Python
Olá, mundo!
~~~

Perceba que ao invés de pular para a próxima linha, foi impresso uma vírgula e um espaço.

O parâmetro sep permite definir o separador entre os argumentos passados na chamada da função print(). Por padrão, o valor de sep é um espaço em branco, mas é possível alterá-lo, como no exemplo abaixo:

~~~Python
print("São", "Paulo", "Futebol", "Clube", sep="-")
~~~

Neste caso, o resultado será:

~~~Python
São-Paulo-Futebol-Clube
~~~

Perceba que ao invés de um espaço em branco, foi impresso um hífen como separador entre as palavras.

Esses parâmetros são opcionais, mas muito úteis em algumas situações, principalmente quando se quer personalizar a saída de texto de acordo com o formato desejado.

---