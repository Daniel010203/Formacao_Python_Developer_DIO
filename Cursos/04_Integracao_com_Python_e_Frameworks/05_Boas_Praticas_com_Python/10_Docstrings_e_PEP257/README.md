# O que são Docstrings e a PEP 257?

## Docstring

Docstring é uma convenção de estilo em Python para documentação de código. É uma string que aparece no início de um módulo, classe, método ou função e contém informações sobre o que o código faz, seus argumentos, valores de retorno e exemplos de uso. O objetivo é ajudar os desenvolvedores a entender o código e facilitar a manutenção e colaboração em projetos.

A docstring é escrita entre aspas triplas (""") e deve seguir o estilo definido pela PEP 257. Ela deve fornecer uma descrição clara e concisa do que o código faz, incluindo uma explicação dos argumentos e valores de retorno. Também pode incluir exemplos de uso e notas adicionais sobre o funcionamento do código.

Um exemplo de docstring para uma função em Python:

~~~py
def calcular_media(numeros):
    """Calcula a média de uma lista de números.

    Argumentos:
    numeros -- uma lista de números

    Retorna:
    A média dos números na lista
    """
    soma = sum(numeros)
    media = soma / len(numeros)
    return media
~~~

---

## PEP 257

A PEP 257 é um guia de estilo da linguagem Python que especifica como escrever docstrings, ou seja, strings de documentação de código em Python. A PEP define uma estrutura e um formato para docstrings que ajuda a garantir a consistência e a legibilidade da documentação do código em projetos Python.

Entre as diretrizes estabelecidas pela PEP 257 estão:

* Use aspas triplas (""") para delimitar docstrings;

* A primeira linha da docstring deve ser um resumo conciso e objetivo do que o código faz;

* Deixe uma linha em branco após o resumo da docstring;

* A partir da segunda linha, explique em mais detalhes o que o código faz, seus argumentos, valores de retorno, exceções lançadas e quaisquer outras informações relevantes;

* Use frases completas e gramaticalmente corretas;

* Evite linhas muito longas;

* Use referências a outros objetos do código, como classes, funções e módulos, dentro da docstring para torná-la mais informativa.

O uso consistente de docstrings em todo o código Python ajuda os desenvolvedores a entender o que o código faz, o que é especialmente importante em projetos de equipe e em projetos de código aberto. Além disso, a documentação do código pode ser gerada automaticamente a partir das docstrings usando ferramentas como o Sphinx.

---