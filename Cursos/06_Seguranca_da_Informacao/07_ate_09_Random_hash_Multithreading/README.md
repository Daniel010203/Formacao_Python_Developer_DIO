# O que é a biblioteca Random, um hash e Multithreading?

### Biblioteca Random

A biblioteca random em Python é um módulo integrado que fornece funções para gerar números aleatórios. Ela permite que os programadores realizem diversas operações relacionadas a aleatoriedade, como a geração de números inteiros aleatórios, seleção aleatória de elementos de uma lista e embaralhamento aleatório de sequências. A biblioteca random utiliza algoritmos para produzir sequências de números aparentemente aleatórios com base em uma semente (seed) inicial. Essa biblioteca é amplamente utilizada em jogos, simulações, criptografia e outras aplicações que requerem aleatoriedade controlada.

---

### Hash

Em computação, uma função de hash é um algoritmo que transforma dados de entrada (como uma string ou um arquivo) em uma sequência de tamanho fixo, geralmente chamada de hash ou valor de hash. O objetivo principal de uma função de hash é mapear os dados de entrada para um valor único que seja praticamente impossível de ser revertido para os dados originais.

Uma função de hash é projetada para produzir um hash único para cada entrada diferente, mas pode acontecer de duas entradas diferentes gerarem o mesmo hash (colisão). No entanto, uma boa função de hash minimiza essas colisões, distribuindo uniformemente os valores de hash possíveis.

Os hashes são amplamente utilizados em várias áreas da computação, como armazenamento e busca de dados, criptografia, verificação de integridade de arquivos e autenticação de senhas. Eles permitem a rápida comparação de grandes quantidades de dados e são essenciais em muitos algoritmos e estruturas de dados eficientes.

Site que encripta e decripta: 
[md5decrypt](http://md5decrypt.net)

*Exemplo*

Crypter
Md5(Hello World !) = b9be3ef4018be19f248f6f8e63b9e006

Decrypter:
b9be3ef4018be19f248f6f8e63b9e006 : Hello World !

---

### Biblioteca hashib

A biblioteca hashlib em Python é usada para calcular hashes criptográficos de dados, como strings ou arquivos. Ela oferece algoritmos seguros, como MD5 e SHA-256, e é útil em segurança, integridade de dados e autenticação.

---

### Multithreading

Multithreading é uma técnica de programação que envolve a execução simultânea de várias threads dentro de um programa. Uma thread representa uma sequência de instruções que pode ser executada independentemente das outras. Ao usar multithreading, um programa pode executar várias tarefas simultaneamente, aproveitando os recursos do sistema de forma mais eficiente.

As threads podem ser executadas em paralelo em sistemas com múltiplos núcleos de processamento ou podem ser alternadas rapidamente em sistemas com apenas um núcleo, criando a ilusão de execução simultânea.

A multithreading é frequentemente usada para melhorar a responsividade de aplicativos, permitindo que tarefas intensivas ou bloqueantes sejam executadas em segundo plano enquanto a interface do usuário permanece interativa. Também é útil para processar tarefas em paralelo, acelerando a execução de programas que podem ser divididos em partes independentes.

No entanto, a programação com multithreading requer cuidados extras, já que várias threads compartilham recursos comuns e podem levar a problemas de concorrência, como condições de corrida e acesso incorreto a dados compartilhados. É necessário sincronizar e coordenar o acesso a recursos compartilhados para evitar comportamentos indesejados e resultados inconsistentes.

---

### Biblioteca ipaddress

A biblioteca "ipaddress" permite que você crie objetos que representam endereços IP individuais, bem como redes IP. Você pode realizar operações como verificação de pertencimento a uma determinada rede, manipulação de sub-redes, cálculo de endereços de broadcast e muito mais.

Com a biblioteca "ipaddress", você pode converter endereços IP entre notações diferentes (como representação decimal pontuada e notação de prefixo CIDR), validar a sintaxe de endereços IP, fazer cálculos aritméticos com endereços IP e realizar outras operações relacionadas a endereços IP e redes.

Essa biblioteca é útil em muitos cenários, como na configuração de redes, análise de log de servidores, criação de ferramentas de gerenciamento de redes e muito mais. Ela simplifica a manipulação e o trabalho com endereços IP e redes em Python.

---

## Aula 08 e 09 - Aulas de Código

*Conferir arquivo:* **gerador_senhas.py**

*Conferir arquivo:* **comparador_hashs.py**

---