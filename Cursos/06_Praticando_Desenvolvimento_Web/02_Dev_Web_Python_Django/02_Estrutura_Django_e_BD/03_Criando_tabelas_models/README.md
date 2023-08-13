## Criando tabelas com models no Django

### Criar classes no models

No Django, você pode criar tabelas no banco de dados definindo classes no arquivo models.py de um aplicativo. Cada classe representa uma tabela, e os atributos da classe definem as colunas dessa tabela. Isso permite que você defina a estrutura do banco de dados usando código Python.

~~~py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
~~~

### Como migrar a classe criada para o banco de dados

Após criar as classes no models.py, você precisa criar migrações para refletir essas alterações no esquema do banco de dados. As migrações contêm instruções SQL que o Django usa para criar ou modificar tabelas. Use o comando python manage.py makemigrations para criar as migrações e python manage.py migrate para aplicá-las ao banco de dados.

~~~bash
python manage.py makemigrations
python manage.py migrate
~~~

### Como alterar uma classe de dados e replicar para o banco de dados

Ao fazer alterações em uma classe já definida no models.py, como adicionar um novo campo, você precisa criar uma nova migração para refletir essas alterações. Novamente, use o comando makemigrations para criar uma migração e migrate para aplicá-la. O Django detectará as diferenças entre o modelo atualizado e o esquema do banco de dados e realizará as alterações necessárias.

~~~bash
python manage.py makemigrations
python manage.py migrate
~~~

### Como registrar a classe no Django Admin

Registrar uma classe no Django Admin permite que você gerencie os registros dessa tabela usando a interface web do Django Admin. Para fazer isso, crie uma classe de administração no arquivo admin.py do seu aplicativo. Você pode usar a função admin.site.register(ClasseDoModelo) para associar o modelo à classe de administração correspondente. Isso permite que você crie, edite e exclua registros dessa tabela através do Django Admin.

~~~py
from django.contrib import admin
from .models import Produto, Cliente

admin.site.register(Produto)
admin.site.register(Cliente)
~~~