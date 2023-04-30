# **06 - Operadores de Associação**

Os operadores de associação em Python são usados para testar se um valor está presente em uma sequência ou coleção de valores. Abaixo está uma lista dos operadores de associação em Python:

* In:
    * Retorna True se o valor especificado está presente na sequência, caso contrário, retorna False.
* Not in:
    * Retorna True se o valor especificado não está presente na sequência, caso contrário, retorna False.

Aqui está um exemplo de como usar esses operadores em Python:

~~~py
x = [1, 2, 3]

# Verificando se um valor está presente na lista
if 2 in x:
    print("2 está presente na lista")
else:
    print("2 não está presente na lista")

# Verificando se um valor não está presente na lista
if 4 not in x:
    print("4 não está presente na lista")
else:
    print("4 está presente na lista")
~~~

Observe que no exemplo acima, o valor "2" está presente na lista "x", portanto, a primeira condição é verdadeira. Por outro lado, o valor "4" não está presente na lista "x", portanto, a segunda condição é verdadeira.

---