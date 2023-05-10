class Passaro():
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Partal está voando!")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa!")


# FIXME: Exemplo ruim do uso de herança para reutilizar o metodo voar()
class Aviao(Passaro):
    def voar(self):
        print("Avião esta decolando!")

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())