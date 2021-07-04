class Player():
    def __init__(self, life, stamina, experience, time, weapon):
        self.life = life 
        self.stamina = stamina 
        self.experience = experience
        self.time = time 
        self.weapon = weapon   
        
    def printStatus(self):
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('                                                                  ')
        print(f'                      \U0001F499 Vida: {self.life}',end="              ")#\U0002764
        print(f'\U0001F525 Energia: {self.stamina}')#\U00026A1
        print(f'                      \U0001F3AF Nivel: {self.experience}',end='             ')
        print(f'\U0001F315 Horário: {self.time}')
        print(f'                               \U0001F5E1 Arma atual: {self.weapon}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')