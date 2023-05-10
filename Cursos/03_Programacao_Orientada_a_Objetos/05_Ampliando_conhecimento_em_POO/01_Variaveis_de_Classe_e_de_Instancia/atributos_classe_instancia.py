class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

alunor_01 = Estudante("Ariel", 1)
alunor_02 = Estudante("Mirella", 2)
mostrar_valores(alunor_01, alunor_02)

Estudante.escola = "Python"
alunor_01.matricula = 3
mostrar_valores(alunor_01, alunor_02)

alunor_03 = Estudante("Garen", 3)
mostrar_valores(alunor_01, alunor_02, alunor_03)