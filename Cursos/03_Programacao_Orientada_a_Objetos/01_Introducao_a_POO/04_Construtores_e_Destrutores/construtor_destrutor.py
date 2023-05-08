class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a classe...")

    def falar(self):
        print("Au au !!!")

def criar_cachorro():
    c = Cachorro("Zeus", "branco", False)
    print(c.nome)

criar_cachorro()
c = Cachorro("Chappie", "Amarelo")
c.falar()

print("Ola mundo!")
print("Ola mundo!")

del c # Força o destrutor 

print("Ola mundo!")
print("Ola mundo!")
print("Ola mundo!")