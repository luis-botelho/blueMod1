from operator import itemgetter
from time import sleep
from datetime import date
def authorizeVote(year):
    """Valida a idade do usuário"""
    atual = date.today().year
    age = atual - year
    if age < 16:
      return 'Negado'
    elif age >= 18 and age < 71:
      return 'Obrigatório'
    elif age < 16 or age > 70:
      return 'Opcional'
def vote(validate, available, unavailable):
    """Usa a validação do usuário e resgitra a opção de voto"""
    choice = 0
    if validate == 'Negado':
        print(f'Infelizmente Você ainda é muito novo para poder votar!')
        pass
    elif validate == 'Obrigatório':
        while choice > 5 or choice < 1:
            print('Escolha um dos candidatos no menu a abaixo:\n[1] Bolsonaro\n[2] Lula\n[3] Batman\n[4] Nulo\n[5] Voto em branco')
            choice = int(input('opção\n'))
    elif validate == 'Opcional':
        option = str(input('Seu voto não é obrigatório deseja votar ?\n').upper().strip())
        if option[0] == "S":
            while choice > 5 or choice < 1:
                print('Escolha um dos candidatos no menu a abaixo:\n[1] Bolsonaro\n[2] Lula\n[3] Batman\n[4] Nulo\n[5] Voto em branco')
                choice = int(input('opção\n'))
        elif option [0] == "N":
            pass
        else:
            print('Você digitou algo errado, voto cancelado!')          

    if choice == 1:
        available['Bolsonaro'] += 1
    elif choice == 2:
        available['Lula'] += 1
    elif choice == 3:
        available['Batman'] += 1
    elif choice == 4:
        unavailable['Nulo'] += 1
    elif choice == 5:
        unavailable['Branco'] += 1

def winner(available,unavailable):
    #"""fase final, transformando o dicionário em uma lista e pegando o vencedor pelo indice"""

    result = available.items()
    winner = sorted(result, key=itemgetter(1))
    print(f'E o candidato escolhido foi',end='')
    sleep(0.5)
    print(f'.',end='')
    sleep(0.5)
    print(f'.',end='')
    sleep(0.5)
    print(f'.',end='')
    sleep(1.0)
    print(f'  {winner[2][0]}!')
    sleep(0.5)
    for key, value in available.items():
        print(f'o candidato {key} teve {available[key]} votos')
    sleep(0.5)
    for key, value in unavailable.items():
        print(f'Tivemos {unavailable[key]} votos {key}')