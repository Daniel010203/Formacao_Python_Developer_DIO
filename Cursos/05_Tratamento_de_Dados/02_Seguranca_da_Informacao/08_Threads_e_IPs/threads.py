from threading import Thread
import time 

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.2)
        print('Piloto: {} Km: {}\n'.format(piloto, trajeto))


t_carro_01 = Thread(target=carro, args=[1, 'Ariel'])
t_carro_02 = Thread(target=carro, args=[2, 'Yan'])

t_carro_01.start()
t_carro_02.start()