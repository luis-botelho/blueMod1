from operator import itemgetter
from time import sleep
def autorizaVoto(year):
    """Valida a idade do usuário"""
    if year < 16:
      return 'Negado'
    elif year >= 18 and year < 71:
      return 'Obrigatório'
    elif year < 16 or year > 70:
      return 'Opcional'
def votacao(validate):
    """Usa a validação do usuário e resgitra a opção de voto"""
    vote = 0
    if validate == 'Negado':
        print(f'Infelizmente Você ainda é muito novo para poder votar!')
        pass
    elif validate == 'Obrigatório':
        while vote > 5 or vote < 1:
            print('Escolha um dos candidatos no menu a abaixo:\n[1] Bolsonaro\n[2] Lula\n[3] Batman\n[4] Nulo\n[5] Voto em branco')
            vote = int(input('opção\n'))
    elif validate == 'Opcional':
        option = str(input('Seu voto não é obrigatório deseja votar ?\n').upper().strip())
        if option[0] == "S":
            while vote > 5 or vote < 1:
                print('Escolha um dos candidatos no menu a abaixo:\n[1] Bolsonaro\n[2] Lula\n[3] Batman\n[4] Nulo\n[5] Voto em branco')
                vote = int(input('opção\n'))
        elif option [0] == "N":
            pass
        else:
            print('Você digitou algo errado, voto cancelado!')          
    return vote
def result(vote,available,unavailable):
    """Pega o voto e adiciona valor ao dicionário"""
    if vote == 1:
        available['Bolsonaro'] += 1
    elif vote == 2:
        available['Lula'] += 1
    elif vote == 3:
        available['Batman'] += 1
    elif vote == 4:
        unavailable['Nulo'] += 1
    elif vote == 5:
        unavailable['Branco'] += 1
def winner(available,unavailable):
    """fase final, transformando o dicionário em uma lista e pegando o vencedor pelo indice"""
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