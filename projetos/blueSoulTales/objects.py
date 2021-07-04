import sys
from time import *
class Status():
    def __init__(self, name, life = 100, stamina = 100, experience = 0, time = 1, weapon = 'Soco'):
        self.life = life 
        self.stamina = stamina 
        self.experience = experience
        self.time = time 
        self.weapon = weapon 
        self.name = name     
    def printStatus(self):
        sys.stdout.write("\033[2J")
        sleep(1.0)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'                                {self.name}                                  ')
        print(f'                      \U0001F499 Vida: {self.life}',end="              ")
        print(f'\U0001F525 Energia: {self.stamina}')#\U00026A1
        print(f'                      \U0001F3AF Nivel: {self.experience}',end='             ')
        print(f'\U0001F315 Horário: {self.time}')
        print(f'                               \U0001F5E1 Arma atual: {self.weapon}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
class Player(Status):
    def __init__(self)
