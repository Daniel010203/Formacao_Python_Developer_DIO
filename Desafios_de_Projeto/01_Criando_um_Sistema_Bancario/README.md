# **Desafios de Projeto**

<img src="https://hermes.dio.me/lab_projects/badges/04769934-e77a-4b20-a779-1e6f7a7ab1c8.png" width="200">

## **Criando um Sistema Bancário com Python**
Nivel: Básico

Conteudo: Conceitos Básicos

Duração: 1h

----
### **DESAFIO**

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escollheu a llinguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

**Objetivo gereal**

Criar um sistema bancário com as operações: 
* Sacar
* Depositar
* Visualizar extrato

---

**Operações**

* Operação de depósito

De ser possível depositar valores positivos para a minha conta bancaria. A v1 do projeto trabalha apenas com 1 usuario, dessa forma não precisamos nos preocupar em identificar qual é o número da agencia e conta bancaria. Todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato.

* Operação de saque

O sistema deve permitir realizar 3 saque diários com imite maximo de R$ 500,00 por saque. Caso o usuario não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não sera possivel sacar o dinheiro por fata de salldo. Todos os saques devem ser armazenados em uma variavel e exibidos na operação extrato.

** Operação de extrato

Essa operação deve listar todos os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atuall da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx

*Exemplos*

1500.45 = R$ 1500.45

---