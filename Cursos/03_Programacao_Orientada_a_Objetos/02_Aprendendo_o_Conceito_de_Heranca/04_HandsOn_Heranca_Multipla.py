class Animal:
    def __init__(self, patas):
        self.patas = patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor, **kw):
        self.cor = cor
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):

        print(Ornitorrinco.__mro__)
        # print(Ornitorrinco.mro())

        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor, patas):
        super().__init__(cor=cor, cor_bico=cor_bico, patas=patas)

gato = Gato(patas=4, cor="preto")
print(gato)

ornitorrinco = Ornitorrinco(patas=2, cor="vermelho", cor_bico="laranja")
print(ornitorrinco)