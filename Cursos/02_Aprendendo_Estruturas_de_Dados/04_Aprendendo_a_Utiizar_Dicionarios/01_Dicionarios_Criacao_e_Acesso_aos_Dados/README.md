# Dicionários: Criação e Acesso aos Dados
---

Em Python, o tipo dicionário é uma estrutura de dados que armazena pares de chave-valor, onde cada chave é única e associada a um valor. Aqui estão algumas características importantes dos dicionários em Python:

~~~py
# Criando um dicionário:

meu_dict = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

# ou

meu_dict = dict(chave1='valor1', chave2='valor2', chave3='valor3')


# Acessando valores em um dicionário:

meu_dict = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
print(meu_dict['chave1']) # saída: 'valor1'


# Adicionando um novo par chave-valor:

meu_dict = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
meu_dict['chave4'] = 'valor4'
print(meu_dict) # saída: {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}


# Alterando um valor em um dicionário:

meu_dict = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
meu_dict['chave2'] = 'novo_valor2'
print(meu_dict) # saída: {'chave1': 'valor1', 'chave2': 'novo_valor2', 'chave3': 'valor3'}


# Removendo um par chave-valor:

meu_dict = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
del meu_dict['chave3']
print(meu_dict) # saída: {'chave1': 'valor1', 'chave2': 'valor2'}


# Verificando se uma chave está em um dicionário:

meu_dict = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
if 'chave1' in meu_dict:
    print("chave1 está presente no dicionário")
else:
    print("chave1 não está presente no dicionário")
~~~

Os dicionários em Python são úteis quando se precisa armazenar pares chave-valor. Eles são especialmente úteis quando se precisa acessar valores com base em chaves, em vez de índices.

---