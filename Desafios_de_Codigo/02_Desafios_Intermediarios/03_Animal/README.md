# **Desafio Intermediário - 2/3 Aproveite a Oferta**
---

## **DESAFIO**

Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1049_b.png" width="300">

**ENTRADA**

A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

**SAIDA**

Imprima o nome do animal correspondente à entrada fornecida.

|Exemplos de Entrada | Exemplo de Saida |
|--------------------|------------------|
|vertebrado mamifero onivoro | homem| 

|Exemplos de Entrada | Exemplo de Saida |
|--------------------|------------------|
|vertebrado ave carnivoro | aguia| 

*Código Base*

~~~py
''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
a = input() 
b = input() 
c = input() 

if a == 'vertebrado': 
    ''' 
    TODO Crie as condições necessárias para definir o tipo de animal possível seguindo
    o esquema da imagem.
    TODO Imprima, de acordo com as condições, o animal identificado.
    '''
elif a == 'invertebrado':
~~~

---