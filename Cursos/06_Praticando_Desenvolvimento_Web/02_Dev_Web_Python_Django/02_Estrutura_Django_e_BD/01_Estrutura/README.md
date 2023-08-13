## Estrutura básica e introdução a banco de dados com o Django-Admin

### Estrutura básica do Django

A estrutura básica do Django segue o padrão de projeto MTV (Model-Template-View), que separa a aplicação em três partes principais. O Model lida com a representação dos dados e a interação com o banco de dados. O Template lida com a apresentação visual e formatação dos dados exibidos ao usuário. O View gerencia a lógica por trás das interações do usuário e coordena a interação entre Model e Template.

### django-admin.py

O django-admin.py é uma ferramenta de linha de comando que permite a administração de projetos Django. Ele pode ser usado para criar projetos, aplicativos, rodar o servidor de desenvolvimento, gerenciar migrações e muito mais.

### manage

O comando manage.py é uma interface para administrar aplicativos Django. Ele é criado automaticamente quando você cria um novo projeto e é usado para executar várias tarefas, como iniciar o servidor de desenvolvimento, criar migrações, criar um superusuário e muito mais.

### wsgi

O WSGI (Web Server Gateway Interface) é uma especificação que define como servidores web se comunicam com aplicativos web Python. O WSGI permite que aplicativos Django sejam executados em servidores web compatíveis, tornando-os acessíveis através da Internet.

### settings

O arquivo settings.py contém as configurações do projeto Django. Isso inclui definições como a configuração do banco de dados, configurações de segurança, configurações de aplicativos e muito mais. É um dos arquivos mais importantes em um projeto Django.

### urls

O mapeamento de URLs para views é definido no arquivo urls.py. Ele direciona as solicitações do usuário para as views apropriadas com base nos padrões de URL definidos. Isso permite a construção de rotas personalizadas para diferentes partes do aplicativo.

### views

As views em Django são responsáveis por processar solicitações do usuário e retornar respostas. Elas contêm a lógica de negócios do aplicativo e interagem com os modelos para buscar ou salvar dados. Uma view pode renderizar um template HTML ou retornar dados em outros formatos, como JSON.

### models

Os models representam a estrutura do banco de dados em um aplicativo Django. Eles definem os tipos de dados e os relacionamentos entre eles. Usando models, é possível criar, recuperar, atualizar e excluir registros no banco de dados de maneira orientada a objetos.

### admin

O Django Admin é uma interface de administração automática que permite gerenciar os dados do aplicativo por meio de uma interface web. Ele utiliza os models definidos para criar uma interface de administração intuitiva, onde é possível adicionar, editar e excluir registros do banco de dados.

### static

A pasta static é usada para armazenar arquivos estáticos, como CSS, JavaScript e imagens. Esses arquivos são servidos diretamente aos clientes e não passam pelo processamento do Django. Eles são usados para estilizar e melhorar a experiência do usuário.

### templates

A pasta templates contém os arquivos de template do Django, geralmente em formato HTML. Os templates são usados para renderizar as views e criar a interface do usuário final. O Django permite a inserção de dados dinâmicos nos templates, tornando a apresentação mais flexível e personalizada.