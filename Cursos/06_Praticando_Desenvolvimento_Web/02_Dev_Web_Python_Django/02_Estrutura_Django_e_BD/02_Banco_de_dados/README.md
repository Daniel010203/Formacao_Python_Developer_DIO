## Banco de dados e Django admin

### Como criar bando de dados com Django admin no Django

Defina seus Modelos: Antes de criar um banco de dados, você precisa definir os modelos que representam as tabelas do banco de dados. Isso é feito em arquivos Python dentro do diretório de um aplicativo Django no arquivo models.py.

~~~Py
# models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
~~~

Crie Migrações: Após definir seus modelos, você precisa criar migrações, que são arquivos que contêm as instruções para criar ou modificar o esquema do banco de dados com base nas alterações nos modelos.
No terminal, execute o seguinte comando:

~~~bash
python manage.py makemigrations
~~~

Aplique as Migrações: Após criar as migrações, você precisa aplicá-las ao banco de dados para criar as tabelas correspondentes.

~~~bash
python manage.py migrate
~~~

Crie um Superusuário: Para acessar o Django Admin e criar registros no banco de dados, você precisa criar um superusuário.

~~~bash
python manage.py createsuperuser
~~~

Acesse o Django Admin: Inicie o servidor de desenvolvimento e acesse o Django Admin no navegador.

~~~bash
python manage.py runserver
~~~

Acesse http://127.0.0.1:8000/admin/ e faça login com as credenciais do superusuário que você criou. Agora, você poderá usar o Django Admin para criar, visualizar, atualizar e excluir registros no banco de dados, com base nos modelos que você definiu.

Lembre-se de que o exemplo acima é simples e serve para ilustrar o processo. Você pode criar modelos mais complexos com relacionamentos entre eles e personalizar o Django Admin para atender às suas necessidades específicas.