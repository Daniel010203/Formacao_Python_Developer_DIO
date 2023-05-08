class Veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print('Ligando o motor...')

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas)
        self.carregado = carregado

    def carregado(self):
        print(f"{'Sim' if carregado else 'Não'} estou carregado!")

minha_moto = Moto("preta", "xxx-0666", 2)
minha_moto.ligar_motor()

meu_carro = Carro("prata", "zzz-0444", 4)
meu_carro.ligar_motor()

meu_caminhao = Caminhao("branco", "yyy-2323", 6, False)
meu_caminhao.ligar_motor()
meu_caminhao.carregado()