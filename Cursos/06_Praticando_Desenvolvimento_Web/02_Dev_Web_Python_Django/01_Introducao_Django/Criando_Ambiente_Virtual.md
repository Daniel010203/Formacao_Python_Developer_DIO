## Criando um Ambiente Virtual no VS Code com virtualenv, Instalando Django e criando um projeto

~~~
pip install virtualenv

virtualenv nome_ambiente_virtual

nome_ambiente_virtual\Scripts\activate
~~~

Se tudo deu certo, ficara algo semelhante a isso:

~~~
(nome_ambiente_virtual) PS C://Users/Seu_Usuario/...

pip install django

pip freeze

django-admin startproject nome_do_projeto

cd nome_do_projeto

python manage.py runserver
~~~

Caso de certo ficara algo semelhante a isso:

~~~
System check identified no issues (0 silenced).
August 06, 2023 - 15:20:04
Django version 4.2.4, using settings 'hello_django.settings'  
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
~~~

Se der erro como esse:

~~~
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
~~~

Tente rodar esse comando:

~~~
python manage.py migrate
~~~

Execute de novo o comando:

~~~
python manage.py runserver
~~~

Agora so continuar segiundo os passos das aulas