## Filtros, tipos de responses e configuraçÕes

### Crar filtros mais elaborados

Ao recuperar dados do banco de dados, você pode aplicar filtros mais elaborados usando a função filter ou exclude. Isso permite que você restrinja os resultados com base em condições específicas.

Exemplo de filtragem com condições mais complexas (views.py):

~~~py
from django.shortcuts import render
from .models import Produto

def produtos_em_promocao(request):
    produtos = Produto.objects.filter(preco__lt=10, disponivel=True)
    return render(request, 'produtos_promocao.html', {'produtos': produtos})
~~~

### Alterar HTML conforme determinada condicional

Nos templates do Django, você pode usar condicionais para alterar o HTML com base em determinadas condições. Isso é útil para exibir conteúdo dinamicamente.

Exemplo de condicional em um template HTML (templates/produtos_promocao.html):

~~~html
<ul>
    {% for produto in produtos %}
        <li>
            {{ produto.nome }} - R$ {{ produto.preco }}
            {% if produto.disponivel %}
                <span class="disponivel">Disponível</span>
            {% else %}
                <span class="indisponivel">Indisponível</span>
            {% endif %}
        </li>
    {% endfor %}
</ul>
~~~

### Configurar Time Zone

A configuração de Time Zone é importante para garantir que as datas e horários em seu aplicativo sejam corretos para a região do usuário.

Configure a Time Zone no arquivo settings.py:

~~~py
TIME_ZONE = 'America/Sao_Paulo'
~~~

### Exceção através Http404 do pacote http.response

Se você precisar gerar uma exceção HTTP 404 (página não encontrada), pode usar o Http404 do pacote django.http.response.

Exemplo de uso do Http404 em uma view (views.py):

~~~py
from django.http import Http404
from .models import Produto

def detalhes_produto(request, produto_id):
    try:
        produto = Produto.objects.get(pk=produto_id)
    except Produto.DoesNotExist:
        raise Http404("Produto não encontrado")
    return render(request, 'detalhes_produto.html', {'produto': produto})
~~~

### Retorno em Json através do JsonResponse do pacote http.response

Se você precisa retornar dados em formato JSON a partir de uma view, pode usar o JsonResponse do pacote django.http.response.

Exemplo de retorno de dados em JSON em uma view (views.py):

~~~py
from django.http import JsonResponse
from .models import Produto

def lista_produtos_json(request):
    produtos = Produto.objects.all()
    data = [{'nome': produto.nome, 'preco': produto.preco} for produto in produtos]
    return JsonResponse(data, safe=False)
~~~

Lembre-se de que esses exemplos são apenas ilustrativos e devem ser ajustados para atender às necessidades e estrutura do seu aplicativo.