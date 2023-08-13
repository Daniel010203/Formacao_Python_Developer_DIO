## Criando uma página de listagem no Django

### Configurar templates

Para criar uma página de listagem no Django, comece configurando os templates. Os templates permitem criar a estrutura visual da página, incorporando dados dinâmicos quando necessário. Defina um diretório chamado templates em seu aplicativo e crie arquivos HTML para suas páginas.

~~~html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <div class="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
~~~

### Criar uma pagina html

Crie uma página HTML que estenderá o template base e substituirá os blocos definidos para o título e o conteúdo. Isso permitirá que você mantenha a consistência visual em todo o site.

~~~html
<!-- templates/listagem.html -->
{% extends "base.html" %}
{% block title %}Lista de Eventos{% endblock %}
{% block content %}
    <h1>Lista de Eventos</h1>
    <!-- Conteúdo da listagem aqui -->
{% endblock %}
~~~

### Listar todos os eventos

No Django, você pode recuperar todos os eventos do banco de dados e passá-los para o template para exibição na página. Isso pode ser feito usando as views e os modelos.

~~~py
# views.py
from django.shortcuts import render
from .models import Evento

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listagem.html', {'eventos': eventos})
~~~

~~~html
<!-- templates/listagem.html -->
{% extends "base.html" %}
{% block title %}Lista de Eventos{% endblock %}
{% block content %}
    <h1>Lista de Eventos</h1>
    <ul>
        {% for evento in eventos %}
            <li>{{ evento.nome }}</li>
        {% endfor %}
    </ul>
{% endblock %}
~~~

### Listar eventos por usuário

Você pode aprimorar a página de listagem para exibir eventos específicos de um usuário, passando o ID do usuário como parâmetro na URL e filtrando os eventos correspondentes no banco de dados.

~~~py
# views.py
from django.shortcuts import render
from .models import Evento

def eventos_por_usuario(request, user_id):
    eventos = Evento.objects.filter(usuario_id=user_id)
    return render(request, 'listagem.html', {'eventos': eventos})
~~~

~~~html
<!-- templates/listagem.html -->
{% extends "base.html" %}
{% block title %}Lista de Eventos{% endblock %}
{% block content %}
    <h1>Lista de Eventos</h1>
    <ul>
        {% for evento in eventos %}
            <li>{{ evento.nome }}</li>
        {% endfor %}
    </ul>
{% endblock %}
~~~