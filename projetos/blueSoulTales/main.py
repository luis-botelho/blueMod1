from objects import Player
import pygame
import sys
import time
pygame.mixer.init()
pygame.mixer.music.load('C:\Github/blueMod1\projetos/blueSoulTales\data/TownTheme.mp3')
pygame.mixer.music.play(-1)

player = Player(100,100,100,'Dia','Espada')
player.printStatus()
input('Grupo 10 é o poder!')
sys.stdout.write("\033[2J")
player.printStatus()
time.sleep(0.5)
input('Esse é um teste de string sobrepor textos no terminal')

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
sys.stdout.write("\033[2J")
sys.stdout.write("\033[A")
player.printStatus()
time.sleep(0.5)
input('Deu certo!')

sys.stdout.write("\033[2J")
sys.stdout.write("\033[A")
player.printStatus()
time.sleep(0.5)
input('Nosso projeto')

sys.stdout.write("\033[2J")
sys.stdout.write("\033[A")
player.printStatus()
time.sleep(0.5)
input('Vai ficar')

sys.stdout.write("\033[2J")
sys.stdout.write("\033[A")
player.printStatus()
time.sleep(0.5)
input('INCRIVEL!')

sys.stdout.write("\033[2J")
sys.stdout.write("\033[A")
player.printStatus()
time.sleep(0.5)
input('Estão preparados para fama e poder ?')