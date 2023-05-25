# Biblioteca Socket

A biblioteca Socket em Python é uma biblioteca padrão que fornece uma interface de programação para comunicação de rede. Ela permite que os programas Python se comuniquem com outros programas em uma rede, usando os protocolos TCP/IP.

Com a biblioteca Socket, é possível criar tanto clientes quanto servidores de rede. Um cliente pode se conectar a um servidor em uma determinada porta e enviar ou receber dados. Por outro lado, um servidor pode ouvir em uma porta específica e aceitar conexões de clientes, permitindo a troca de dados entre eles.

A biblioteca Socket oferece diferentes classes e métodos para facilitar a comunicação de rede. As principais classes são socket, socketserver e select. A classe socket é usada para criar e gerenciar soquetes de rede, enquanto a classe socketserver facilita a implementação de servidores TCP/IP. A classe select fornece uma maneira eficiente de lidar com várias conexões simultâneas.

Ao utilizar a biblioteca Socket, é possível estabelecer conexões de rede, enviar e receber dados, definir opções de soquete, tratar erros de conexão e gerenciar eventos assíncronos, entre outras funcionalidades relacionadas à comunicação de rede.

Em resumo, a biblioteca Socket em Python é uma ferramenta essencial para desenvolver aplicativos de rede, permitindo a comunicação entre programas por meio de protocolos TCP/IP. Com ela, é possível implementar tanto clientes quanto servidores de maneira eficiente e flexível.

---

## TCP

TCP (Transmission Control Protocol) é um protocolo confiável e orientado à conexão usado para transmitir dados de forma segura e ordenada em redes de computadores. Ele garante a entrega confiável dos dados, controla o fluxo e evita congestionamentos. O TCP divide os dados em segmentos e usa endereços IP e números de porta para identificar remetentes e destinatários. É amplamente usado em aplicativos que exigem transferência segura de dados.

---

## UDP

UDP (User Datagram Protocol) é um protocolo de transporte não confiável e sem conexão. Ele não garante a entrega confiável dos dados, não controla o fluxo ou o congestionamento da rede e não estabelece uma conexão antes da transmissão. O UDP é usado em aplicativos que priorizam a velocidade em vez da confiabilidade, como streaming de mídia e jogos online.

---

## Aulas de Código

4. Desenvolvimento de um cliente TCP
    * *Conferir arquivo:* **01_tcp.py**

5. Desenvolvimento de um cliente UDP
    * *Conferir arquivo:* **02_cliente_udp.py**

6. Desenvolvimento de um Servidor
    * *Conferir arquivo:* **03_server_udp.py**

---