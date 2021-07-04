
from time import *

def part1():
    part1 = 'Mais um dia se passou no reino Blue Soul, você está apreciando o crepúsculo apor um longo dia de trabalho de campo, e o único que consegue sentir é que esse não é o seu lugar. Você sonha com aventuras, desafios e conquistas. A vida de um simples plebeu não é mais suficiente para você, mas a partir de hoje tudo vai mudar, agora você está decidido a realizar as escolhas necessárias para mudar a sua vida e se tornar o maior cavalheiro do reino.'
    for i in part1:
        sleep(0.1)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar')
def part2():
    part2 = 'A lua cheia nasce no horizonte, iluminando os vastos campos ao seu redor, de repente o galopar de um cavalo ecoa pelo silencio do campo, atraído pelas suaves brisas do verão. La distante, onde começa a floresta sem fim, emerge um cavalo branco, refletindo a luz do luar, manchado com a sangue do seu cavalheiro que sobre ele varia entre a vida e a morte. Sem duvidar você corre na direção do seu encontro esperando poder evitar o destino desse cavalheiro.'
    for i in part2:
        sleep(0.1)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar')
def part3():
    part3 = 'Enquanto a distancia entre vocês é encurtada a vida do cavalheiro é perdida a cada galopar do seu cavalo, para quando seu encontro sucede o destino já está traçado. O cavalo cansado e machucado para frente a você, seu instinto indica que já está fora de perigo, sobre ele esta o corpo sem vida do seu companheiro.'
    for i in part3:
        sleep(0.1)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar')
def menu1():
    choice = input('[1] Retirar o corpo e deitar ele no chão.\n[2] Buscar pertences de valor e abandonar o cavalo e o corpo.\n[3] Pegar a espada do cavalheiro por se aparece alguém ou algo.\n\nFaça sua escolha:\n')
    if choice == 1:
        choice = input('[1] Buscar pertences de valor e abandonar o cavalo e o corpo.\n[2] Pegar a espada do cavalheiro por se aparece alguém ou algo.\n\nFaça sua escolha:\n')
        if choice == 1:
            return 2
        elif choice == 2:
            return 3
    elif choice == 2:
        return 2
    elif choice == 3:
        return 3