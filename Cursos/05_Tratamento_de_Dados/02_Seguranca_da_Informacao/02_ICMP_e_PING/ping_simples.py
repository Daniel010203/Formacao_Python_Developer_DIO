import os # Importa o módulo ou bbiblioteca "os"
# Integra os programas e recursos do Sistema Operacional

print("#" * 60)

# Variavel que vai receber do usuario um IP ou HOST
ip_ou_host = input("Digite o IP ou HOST a ser verificado: ")

print("-" * 60)

# Chamando o módulo system da biblioteca "os"
# Usando o comando ping -n -num de pacotes que serao 6 {}
os.system("ping -n 6 {}".format(ip_ou_host))

print("#" * 60)