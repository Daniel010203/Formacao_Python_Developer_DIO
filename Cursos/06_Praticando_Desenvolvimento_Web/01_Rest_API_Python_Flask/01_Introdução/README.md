## Introdução ao Rest Api com Flask

### O que é API?

API é a sigla para "Interface de Programação de Aplicativos" (Application Programming Interface). É um conjunto de regras e protocolos que permite a comunicação e interação entre diferentes sistemas de software. As APIs definem os métodos e formatos de dados que um aplicativo pode usar para solicitar ou enviar informações a outro aplicativo ou serviço online. Elas possibilitam a integração entre sistemas e facilitam o desenvolvimento de aplicações, pois permitem que os desenvolvedores utilizem funcionalidades de outros programas sem precisar conhecer todos os detalhes de sua implementação interna. As APIs são amplamente utilizadas na construção de aplicativos web, móveis e de desktop, bem como no funcionamento de serviços e plataformas na internet.

---

### O que é REST?

REST (Representational State Transfer) é um estilo arquitetural usado para projetar sistemas de comunicação entre computadores, especialmente em aplicações web. Ele define um conjunto de princípios e restrições que devem ser seguidos para criar APIs web eficientes e escaláveis.

Os principais princípios do REST incluem:

* Recursos Identificados por URLs: 

Cada recurso (informação ou funcionalidade) deve ser representado por uma URL única e específica.

* Uso de Métodos HTTP: 

As operações padrão do HTTP (GET, POST, PUT, DELETE, etc.) são usadas para manipular os recursos representados pelas URLs.

* Sem Estado (Stateless): 

Cada solicitação para o servidor deve conter todas as informações necessárias para entendê-la, sem depender de estados de sessão anteriores. Isso torna as solicitações independentes e mais facilmente escaláveis.

* Operações CRUD: 

As APIs REST geralmente implementam operações CRUD (Create, Read, Update, Delete), permitindo a criação, leitura, atualização e exclusão de recursos.

* Representações de Recursos:

Os recursos podem ser representados em diferentes formatos, como JSON, XML ou HTML, dependendo do tipo de dados que a aplicação cliente necessita.

* Uso de Hypermedia (HATEOAS): 

O servidor fornece links hipermídia nos recursos retornados, permitindo que o cliente navegue pela API dinamicamente, descobrindo e acessando recursos relacionados.

Essas restrições tornam as APIs RESTful mais simples, flexíveis e fáceis de serem consumidas por diferentes plataformas e dispositivos. As APIs REST são amplamente utilizadas na construção de serviços web, especialmente em aplicações web modernas, aplicativos móveis e integrações entre sistemas distribuídos.

---

### O que é REST API?

Uma REST API é uma interface que segue os princípios do estilo arquitetural REST, permitindo que diferentes sistemas se comuniquem através de solicitações HTTP. Ela usa URLs para identificar recursos e métodos HTTP para realizar operações sobre esses recursos. As REST APIs são amplamente usadas em aplicações web e serviços para troca de informações de forma padronizada e eficiente.

---

### Principais Métodos do Protocolo HTTP

* GET - Método que solicita algum recurso ou objeto do servidor por meio da URI.
* POST - Método usado para envio de arquivo/dados ou formulário HTML para o servidor.
* PUT - Aceitar criar ou modificar um objeto do servidor.
* DELETE - Informar por meio da URI o objeto a ser deletado.

---

### URL vs URN vs URI?

URL, URN e URI são conceitos relacionados à identificação e localização de recursos na internet:

* URL (Uniform Resource Locator): 

É uma forma específica de URI (Uniform Resource Identifier) que descreve a localização de um recurso na internet. A URL inclui o esquema (protocolo), o domínio (endereço do servidor) e, opcionalmente, o caminho para o recurso e outros parâmetros. Exemplo: https://www.example.com/pagina.html

* URN (Uniform Resource Name): 

É outro tipo de URI que fornece um nome único e permanente para identificar um recurso. Ao contrário das URLs, as URNs não indicam a localização do recurso, apenas o seu nome. URNs são mais utilizadas em contextos onde a localização pode mudar ao longo do tempo, mas o nome deve permanecer constante. Exemplo: urn:isbn:0451450523

* URI (Uniform Resource Identifier): 

É um termo genérico que abrange tanto URLs quanto URNs. É uma sequência de caracteres que identifica de forma única um recurso na internet. URIs podem ser usadas para identificar recursos e fornecer um meio de acesso a eles.

Em resumo, URI é o termo mais amplo que engloba tanto URLs quanto URNs. URLs são usadas para identificar e localizar recursos na internet, enquanto URNs fornecem apenas um nome único para identificação, sem indicar sua localização.

---

### XML - Extensible Markup Language

XML (Extensible Markup Language) é uma linguagem de marcação que foi projetada para armazenar e transportar dados de forma legível tanto para humanos quanto para máquinas. Ela permite que você crie documentos com tags personalizadas para definir a estrutura e o significado dos dados dentro do documento.

*Exemplo de Código:*

~~~xml
<pessoas>
  <pessoa>
    <nome>John</nome>
    <idade>30</idade>
    <cidade>New York</cidade>
  </pessoa>
  <pessoa>
    <nome>Mary</nome>
    <idade>25</idade>
    <cidade>London</cidade>
  </pessoa>
  <pessoa>
    <nome>Carlos</nome>
    <idade>28</idade>
    <cidade>São Paulo</cidade>
  </pessoa>
</pessoas>
~~~

---

### JSON - JavaScript Object Notation

JSON (JavaScript Object Notation) é um formato leve de intercâmbio de dados que se tornou muito popular na web e no desenvolvimento de aplicativos. É baseado em uma sintaxe simples de pares de chave-valor e é fácil de ser lido tanto por humanos quanto por máquinas.

*Exemplo de Código:*

~~~json
{
  "nome": "João",
  "idade": 25,
  "cidade": "São Paulo",
  "amigos": ["Maria", "Carlos"],
  "trabalha": true
}

~~~

---

### Flask

Flask é um microframework web em Python. Ele foi projetado para ser simples, leve e flexível, permitindo que os desenvolvedores criem rapidamente aplicativos web sem a complexidade de um framework completo. Flask oferece o mínimo necessário para criar aplicações web, fornecendo roteamento, manipulação de requisições e respostas HTTP, além de suporte a extensões para adicionar funcionalidades adicionais conforme necessário. É amplamente utilizado para a criação de APIs RESTful, sites e serviços web de pequeno a médio porte, sendo uma escolha popular para projetos que valorizam a simplicidade e o controle do desenvolvedor.

*Exemplo de Código*

~~~
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return u'Olá mundo!'

if __name__ == "__main__":
    app.run()
~~~

---