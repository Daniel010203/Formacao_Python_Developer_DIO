## Criando uma API com Flask no Ambiente COLAB

[Google COLAB - Site](https://colab.research.google.com)


### Instalando e utilizando Django no Google Colab

Códigos usados em aula para criar uma porta com acesso a nossa maquina, instalar o django e usaar o colab.

~~~py
pip install o django

!django-admin startproject aula_dio

%cd aula_dio/

from google.colab.output import eval_js
print(eval_js("google.colab.kernel.proxyPort(8000)"))

!python manage.py runserver 8000
~~~

*Google Colab e Django* - [Link da aula](https://colab.research.google.com/drive/1LdczuS0VO8bEQBxkc4F31Ow1GSp6_Uyj)


---

### Integração da biblioteca FastAPI com Flask na Plataforma Colab

FastAPI:

O FlaskAPI é uma extensão do Flask, um framework web em Python, que simplifica o desenvolvimento de APIs. Ele fornece recursos para criar, gerenciar e controlar APIs de forma eficiente, incluindo roteamento, serialização de dados, autenticação, validação de entrada, manipulação de erros e suporte a diferentes métodos HTTP. É uma opção popular para criar APIs em Python devido à sua simplicidade e flexibilidade.

*Aula teorica sobre FastAPI* - [Link da aula](https://colab.research.google.com/drive/1eJLK11jRcHJdVB0-K0eHxgI73NdFxyW3)

---

### Projeto API Flask no Google Colab: Integrando um arquivo JSON para um servidor FastAPI

*Projeto* - [Link da Aula](https://colab.research.google.com/drive/1g2hsz6uy753AJlSORImhYu_stt69twsP)

Código feito em aula

~~~py
!pip install flask_ngrok

import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk

app = Flask(__name__) #the name of the application package
run_with_ngrok(app) 

d = {
    "name": "Nikola", 
    "surname": "Tesla", 
    "idade": 60
      }

@app.route("/") #code to assign HomePage URL in our app to function home.

def home():
  '''
  The entire line below must be written in a single line.
  '''
  return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3></marquee>"

@app.route("/input") #code to assign Input URL in our app to function input.

def input():
  return jsonify(d) # "d" is the dictionary we defined

@app.route('/output', methods=['GET','POST']) #output page

def predJson():
 pred = r.choice(["positive","negative"])
 nd = d # our input
 nd["prediction"]=pred
 return jsonify(nd)

app.run()

~~~

---

### DESAFIO DE PROJETO

Para este projeto o desafio final envolve a entrega de uma API desenvolvida no framework Flask utilizando a Plataforma COLAB. O Objetivo principal está relacionado com a leitura de uma planilha de dados no formato JSON utilizando uma API no ambiente de desenvolvimento colaborativo COLAB.

Nosso servidor FastAPI deve trazer a planilha gerada em JSON, assim, como estamos apresentando um “Hello Word” neste exemplo. Para isso, deve ser dado um {Public_URL}/index no navegador para chegar ao nosso endpoint, pois criamos apenas uma rota, ou seja , /index.

---