## Conhecendo a Linguagem de Programação Python

*Documentação de estudos - **Ariel Riello***

---

### **Variáveis e Constantes**

---

Variáveis e constantes são elementos básicos da programação em Python (e em outras linguagens de programação). Aqui está uma breve descrição sobre variáveis e constantes em Python:

* **Variáveis:**
    * Uma variável é um espaço de memória reservado para armazenar um valor. O valor armazenado pode ser modificado ao longo do tempo, tornando as variáveis úteis para armazenar dados que mudam durante a execução do programa. Em Python, as variáveis são criadas ao atribuir um valor a um nome. O tipo da variável é inferido automaticamente pelo interpretador do Python com base no valor atribuído.

* **Constantes:**
    * Uma constante é um valor que não muda durante a execução do programa. Em Python, as constantes são definidas usando uma variável, mas com um valor que não será modificado durante a execução do programa. É uma convenção utilizar letras maiúsculas para definir constantes em Python, embora não haja nada que impeça a modificação de seu valor.

Vale lembrar que em Python, a nomenclatura de variáveis e constantes é igual. Ou seja, é possível reatribuir um novo valor a uma variável previamente criada, que antes continha um valor diferente. No entanto, para indicar que um nome de variável é uma constante, convenciona-se em utilizar letras maiúsculas, deixando o código mais claro.

~~~Python
# Exemplo de variável
mensagem = "Olá, mundo!"
print(mensagem)

# Reatribuição do valor da variável
mensagem = "Olá, pessoal!"
print(mensagem)

# Exemplo de constante
PI = 3.14159
raio = 5
area = PI * (raio ** 2)
print("A área do círculo é:", area)

# Tentativa de reatribuir o valor da constante (gera erro)
PI = 3.14
~~~

No exemplo acima, a variável "mensagem" é criada e atribuída o valor "Olá, mundo!". Em seguida, o valor da variável é alterado para "Olá, pessoal!" e, em seguida, impresso na tela.

Já a constante "PI" é definida com o valor 3.14159 e utilizada no cálculo da área de um círculo, que é impressa na tela. Ao tentar reatribuir o valor da constante "PI", é gerado um erro, pois em Python as constantes não podem ser modificadas após a definição.

---

**Snake Case** - Boas Práticas

Snake case é uma convenção de nomenclatura de variáveis em Python. Nesta convenção, as palavras são separadas por um caractere de sublinhado "_", tornando o nome da variável mais legível.

Por exemplo, ao invés de utilizar nomes como "nomeDaVariavel" ou "NomeDaVariavel", que podem tornar a leitura mais difícil, é recomendado utilizar o snake case: "nome_da_variavel".

Essa convenção é bastante utilizada em Python, sendo adotada por muitos desenvolvedores e pela própria comunidade Python. Vale lembrar que, embora seja uma convenção, não é uma regra obrigatória. É possível utilizar outras convenções de nomenclatura, desde que sejam claras e consistentes dentro do projeto.

---