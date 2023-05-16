# Principais Diretrizes da PEP 8

A PEP 8 é uma especificação técnica que define as convenções de estilo de código para a linguagem Python. Algumas das principais diretrizes da PEP 8 incluem:

* Utilizar espaços em vez de tabulações para indentação. Cada nível de indentação deve ter 4 espaços.

* Utilizar nomes descritivos e significativos para variáveis, funções, módulos, classes e métodos.

* Utilizar letras minúsculas separadas por sublinhados (_snake_case) para nomes de funções, variáveis e módulos.

* Utilizar letras maiúsculas separadas por sublinhados (_CamelCase) para nomes de classes.

* Limitar a largura de linhas de código a 79 caracteres.

* Utilizar duas linhas em branco entre funções e classes.

* Utilizar espaços em branco em torno de operadores e após vírgulas em listas, tuplas e argumentos de funções.

* Utilizar docstrings para documentar funções, classes e módulos.

* Importar módulos em linhas separadas e agrupar os mesmos em seções (biblioteca padrão, pacotes de terceiros, módulos locais).

* Evitar código desnecessário, como imports não utilizados e variáveis não utilizadas.

Essas são algumas das principais diretrizes da PEP 8, que visam tornar o código Python legível, consistente e fácil de manter. É importante seguir essas diretrizes ao escrever código em Python para garantir que o mesmo possa ser facilmente compreendido e mantido por outros desenvolvedores.

---

# Code Layout

Exemplo de código em Python com uma boa organização seguindo as diretrizes da PEP 8:

~~~py
# Imports da biblioteca padrão
import os
import sys
import datetime

# Imports de pacotes de terceiros
import pandas as pd
from flask import Flask, jsonify

# Imports de módulos locais
from utils import load_data, clean_data
from models import MyModel

# Constantes
MY_CONSTANT = 42

# Variáveis globais
my_var = "Hello, world!"

# Funções
def my_function(arg1, arg2):
    """
    Esta é uma função que faz algo útil.
    """
    result = arg1 + arg2
    return result

# Classes
class MyClass:
    """
    Esta é uma classe que faz algo útil.
    """
    def __init__(self, arg1):
        self.arg1 = arg1
    
    def my_method(self):
        """
        Este é um método que faz algo útil.
        """
        return self.arg1 + MY_CONSTANT

# Aplicação Flask
app = Flask(__name__)

@app.route("/")
def home():
    """
    Endpoint da aplicação Flask.
    """
    data = load_data()
    cleaned_data = clean_data(data)
    model = MyModel()
    prediction = model.predict(cleaned_data)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
~~~

Nesse exemplo, podemos observar os seguintes pontos importantes para uma boa organização seguindo a PEP 8:

Imports são organizados em seções (biblioteca padrão, pacotes de terceiros e módulos locais) e importados em linhas separadas.

* Letras minúsculas separadas por sublinhados são utilizadas para nomes de funções, variáveis e módulos.

* Letras maiúsculas separadas por sublinhados são utilizadas para nomes de classes.

* Constantes são definidas em maiúsculas.

* Variáveis globais são definidas no topo do arquivo.

* Funções são definidas antes de classes.

* Docstrings são utilizados para documentar funções, classes e módulos.

* Linhas de código são limitadas a 79 caracteres de largura.

* Espaços em branco são utilizados em torno de operadores e após vírgulas em listas, tuplas e argumentos de funções.

Essas são algumas das diretrizes da PEP 8 que são utilizadas no exemplo acima. O objetivo é tornar o código Python mais legível e consistente, facilitando a manutenção e colaboração entre desenvolvedores.

---