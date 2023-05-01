# **Desafios Básicos**

<img src="https://hermes.dio.me/code_challenge/badge/503d2467-4220-41b0-9423-ec8f6c8e1d38.png" width="200">

## **Encaixa ou Não 3/3**
Nivel: Básico

Conteudo: Conceitos Básicos

Duração: 1h

----
### **DESAFIO**

Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

**ENTRADA**

A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

**SAIDA**

Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

---

>*Exemplo de Entrada* | *Exemplo de Saida* |
> --- | ---
> 4 | encaixa 
> 56234523485723854755454545478690  | nao
> 78690 | encaixa
> 5434554 543 | encaixa
> 1243 1243 | nao
> 54 64545454545454545454545454545454554 | encaixa



---
*Codigo Base*

~~~py
''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
N = int(input())

while(n > 0):
    ''' 
    TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
    "encaixa" ou "não encaixa" para cada uma das relações N vezes.
    '''
~~~
---