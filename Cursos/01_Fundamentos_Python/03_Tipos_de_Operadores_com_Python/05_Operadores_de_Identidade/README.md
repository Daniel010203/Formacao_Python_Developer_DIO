# **05 - Operadores de Identidade**

Os operadores de identidade em Python são usados para comparar objetos com base em sua identidade, ou seja, se eles se referem ao mesmo objeto na memória. Abaixo está uma lista dos operadores de identidade em Python:

* É (is): 
    * Retorna True se ambos os operandos se referem ao mesmo objeto na memória, caso contrário, retorna False.

* Não é (is not):
    * Retorna True se ambos os operandos não se referem ao mesmo objeto na memória, caso contrário, retorna False.

Aqui está um exemplo de como usar esses operadores em Python:

~~~py
x = [1, 2, 3]
y = [1, 2, 3]

# Comparando a identidade dos objetos
if x is y:
    print("x e y se referem ao mesmo objeto")
else:
    print("x e y não se referem ao mesmo objeto")

# Comparando a não identidade dos objetos
if x is not y:
    print("x e y não se referem ao mesmo objeto")
else:
    print("x e y se referem ao mesmo objeto")
~~~

Observe que no exemplo acima, embora as listas "x" e "y" tenham os mesmos valores, elas não se referem ao mesmo objeto na memória. Portanto, a primeira condição é falsa e a segunda condição é verdadeira.

---