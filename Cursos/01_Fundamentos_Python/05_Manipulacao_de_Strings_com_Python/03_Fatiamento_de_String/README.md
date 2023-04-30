# **Fatiamento de String**
---

O fatiamento de string em Python é uma operação que permite selecionar uma parte de uma string, especificando um intervalo de índices. É possível obter uma substring de uma string maior, pegando um intervalo de caracteres. O fatiamento de string é realizado usando a sintaxe string[inicio:fim], onde inicio é o índice inicial da substring e fim é o índice final (não incluído) da substring. Aqui está um exemplo de código:

~~~py
frase = "O rato roeu a roupa do rei de Roma"

# Selecionando os primeiros 5 caracteres da string
print(frase[:5]) # Saída: O rat

# Selecionando os últimos 5 caracteres da string
print(frase[-5:]) # Saída:  de Roma

# Selecionando cada segundo caractere da string
print(frase[::2]) # Saída: Ortrouadrpd em e oad

# Selecionando uma substring a partir da posição 12 até o final da string
print(frase[12:]) # Saída: a roupa do rei de Roma

# Selecionando uma substring que começa 4 caracteres antes do final da string
print(frase[-4:]) # Saída: Roma
~~~

---