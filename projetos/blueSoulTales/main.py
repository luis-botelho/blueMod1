from projetos.blueSoulTales.Hist import part3
from objects import *
from Hist import *
from pygame import *

import sys
from time import*
mixer.init()
mixer.music.load('C:\Github/blueMod1\projetos/blueSoulTales\data/TownTheme.mp3')
mixer.music.play(-1)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Bem vindo(a) a Blue Soul')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
input('Aperte enter para continuar')
sys.stdout.write("\033[2J")
sleep(0.5)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
name = input('Qual nome do jogador ?:\n').title()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
sys.stdout.write("\033[2J")
sleep(1.0)
status = Status(name)
status.printStatus()
part1()
status.printStatus()
part2()
status.printStatus()
part3()
status.printStatus()
menu1()

