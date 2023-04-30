# **Operadores Lógicos**
Os operadores lógicos em Python são usados para comparar valores booleanos e retornar um valor booleano (verdadeiro ou falso) com base na lógica booleana. Abaixo está uma lista dos operadores lógicos em Python:

* E lógico (and):
    * Retorna True se ambos os valores comparados forem True, caso contrário, retorna False.
* OU lógico (or):
    * Retorna True se pelo menos um dos valores comparados for True, caso contrário, retorna False.
* NÃO lógico (not):
    * Retorna o oposto do valor booleano (True ou False) do operando.

Aqui está um exemplo de como usar esses operadores em Python:

~~~py
x = 10
y = 3

# E lógico
if x > 5 and y > 2:
    print("Ambas as condições são verdadeiras")

# OU lógico
if x > 5 or y > 5:
    print("Pelo menos uma das condições é verdadeira")

# NÃO lógico
if not x == y:
    print("x não é igual a y")
~~~

Observe que no primeiro exemplo, a condição é verdadeira porque tanto "x > 5" quanto "y > 2" são verdadeiros. No segundo exemplo, a condição é verdadeira porque "x > 5" é verdadeiro, mesmo que "y > 5" seja falso. No terceiro exemplo, a condição é verdadeira porque "x" não é igual a "y".

---

*Códigos feitos em aula*

~~~py
print(False or False or False)

saldo = 100
saque = 250
limite = 200
conta_especial = True

exp = saldp >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite> or (conta_especiall and saldo >=saque)
print(exp_2))

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
~~~

---