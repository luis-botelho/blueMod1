# from random import randint
# class Lancador():
#     def __init__(self, lados):
#         if lados == 'Moeda':
#             self.lados = 2
#         elif lados == 'Dado':
#              self.lados = 6
#     def lancar(self):
#         jogo = randint(0,self.lados)
#         return print(jogo)

# escolha = str(input('escolha dado ou moeda: '.title().strip()))
# player = Lancador(escolha)
# player.lancar()  
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. 
# No final tudo isso será guardado em um dicionário, incluindo a média de gols por jogo, e o total 
# de gols feitos durante o campeonato
final = {}
gols = []

name = str(input('Qual nome ? :' ))
games = int(input('Quantas partidas jogou ?: '))
for i in range(games):
    gol = int(input('Quantos jogos fez nessa partida ?: '))
    gols.append(gol)
final[name] = [(sum(gols) / games), sum(gols)]
print(final)

class Jogador():
    from time import sleep
    def __init__(self,nome,partidas):
        self.nome =  nome
        self.partidas = partidas

    def calculo(self,dic):
        gols = []
        for i in range(self.partidas):
            gol = int(input('Quantos jogos fez nessa partida ?: '))
            gols.append(gol)
            dic[self.nome] = [(sum(gols) // games), sum(gols)]
        return print(f'O jogador {self.nome}, fez uma media de {dic[self.nome][0]}, gols por partida, com um total de {dic[self.nome][1]} gols')
jogos = {}
condition =''
while condition[0] != 'N':
    name = str(input('Qual nome do jogador ? :' ))
    games = int(input('Quantas partidas jogou ?: '))
    jogador = Jogador(name, games)
    jogador.calculo(jogos)
    condition = str(input('Deseja adicionar outro jogardor ?').upper().strip()) 