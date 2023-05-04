# **Desafios Básicos**

<img src="https://hermes.dio.me/code_challenge/badge/503d2467-4220-41b0-9423-ec8f6c8e1d38.png" width="200">

## **Tuitando 1/3**
Nivel: Básico

Conteudo: Conceitos Básicos

Duração: 1h

----
### **DESAFIO**

O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

**ENTRADA**

A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

**SAIDA**

A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

---

*Exemplo de Entrada*
>RT @TheEllenShow: If only Bradley's arm was longer. Best photo ever. #oscars pic.twitter.com/C9U5NOtGap

*Exemplo de Saida*
> TWEET

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
T = input()
    ''' 
    TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
    Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".
    '''
~~~
---