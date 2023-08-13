## Realizando inserção de dados

### Criar página para submit da inserção

Para realizar a inserção de dados em seu aplicativo Django, você precisa criar uma página que permita aos usuários enviar os dados. Isso envolve a criação de um formulário HTML e a configuração de uma view para lidar com a submissão desse formulário.

Exemplo de página HTML (templates/inserir_dados.html):

~~~html
<form method="post" action="{% url 'inserir_dados' %}">
    {% csrf_token %}
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome">
    <label for="idade">Idade:</label>
    <input type="number" id="idade" name="idade">
    <button type="submit">Enviar</button>
</form>
~~~

### Função creat

No Django, a função create é usada para criar e salvar registros em um modelo. Ela simplifica o processo de criação de objetos e persistência no banco de dados.

Exemplo de uma view que utiliza a função create para inserção de dados (views.py):

~~~py
from django.shortcuts import render, redirect
from .models import Pessoa

def inserir_dados(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        Pessoa.objects.create(nome=nome, idade=idade)
        return redirect('lista_pessoas')  # Redireciona para a lista de pessoas
    return render(request, 'inserir_dados.html')
~~~

Nesse exemplo, a função create é usada para criar um novo objeto Pessoa no banco de dados com base nos dados enviados pelo formulário. Certifique-se de que os campos no modelo Pessoa correspondam aos campos no formulário HTML.

Lembre-se de ajustar os nomes dos modelos, campos e URLs de acordo com a estrutura do seu aplicativo.