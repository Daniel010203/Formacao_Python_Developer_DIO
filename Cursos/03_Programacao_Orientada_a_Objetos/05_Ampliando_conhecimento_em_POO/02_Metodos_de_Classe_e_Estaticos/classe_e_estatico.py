class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def data_nascimento_idade(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade)
    
    @staticmethod
    def de_maior(idade):
        return idade >= 18
    
p = Pessoa.data_nascimento_idade(1992, 6, 9, "Ariel")
print(p.nome, p.idade)

print(Pessoa.de_maior(18))
print(Pessoa.de_maior(10))