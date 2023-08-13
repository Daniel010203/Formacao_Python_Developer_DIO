## Alterando, excluindo e filtrando dados do banco de dados no django

### Realizando alterações e exclusão de dados

Para alterar ou excluir dados do banco de dados no Django, você precisa criar views e templates que permitam ao usuário interagir com essas ações. Isso normalmente envolve a criação de links ou botões nas páginas e o tratamento das ações correspondentes nas views.

### Criar rotas para edição e exclusão

Crie rotas (URLs) para as páginas de edição e exclusão dos registros. Essas URLs apontarão para as views que executarão as operações de alteração e exclusão.

Exemplo de URLs (urls.py):

~~~py
from django.urls import path
from . import views

urlpatterns = [
    path('editar/<int:id>/', views.editar_dados, name='editar_dados'),
    path('excluir/<int:id>/', views.excluir_dados, name='excluir_dados'),
]
~~~

### Reaproveitamento de template de inclusão para realizar a alteração

Para realizar a alteração de dados, você pode reutilizar o mesmo formulário de inserção, mas com os campos já preenchidos com os valores atuais. Isso pode economizar tempo e manter a consistência visual.

### Função delete

A função delete é usada para excluir um registro do banco de dados com base em um critério específico.

Exemplo de uma view que utiliza a função delete para excluir dados (views.py):

~~~py
from django.shortcuts import render, redirect
from .models import Pessoa

def excluir_dados(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('lista_pessoas')  # Redireciona para a lista de pessoas
~~~

### Função update

A função update é usada para atualizar os valores de um ou mais campos em um registro do banco de dados.

Exemplo de uma view que utiliza a função update para alterar dados (views.py):

~~~py
from django.shortcuts import render, redirect
from .models import Pessoa

def editar_dados(request, id):
    pessoa = Pessoa.objects.get(id=id)
    
    if request.method == 'POST':
        pessoa.nome = request.POST['nome']
        pessoa.idade = request.POST['idade']
        pessoa.save()
        return redirect('lista_pessoas')  # Redireciona para a lista de pessoas
    
    return render(request, 'editar_dados.html', {'pessoa': pessoa})
~~~

Nesse exemplo, a função update não é usada diretamente; em vez disso, usamos save para aplicar as alterações ao registro existente.

Lembre-se de ajustar os nomes dos modelos, campos e URLs de acordo com a estrutura do seu aplicativo.