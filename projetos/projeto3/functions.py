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
def apuracao(choice):
    """Transforma o valor int digitado em um string para poder adicionar no dicionário"""
    candidate = ""
    if choice == 1:
        candidate = 'Bolsonaro'
    elif choice == 2:
        candidate = 'Lula'
    elif choice == 3:
        candidate = 'Batman'
    elif choice == 4:
        candidate = 'Nulo'
    elif choice == 5:
        candidate = 'Branco'
    return candidate
def result(vote,available,unavailable):
    """Adiciona conforme o voto valor ao dicionário"""
    if vote == 'Bolsonaro':
        available['Bolsonaro'] += 1
    elif vote == 'Lula':
        available['Lula'] += 1
    elif vote == 'Batman':
        available['Batman'] += 1
    elif vote =='Nulo':
        unavailable['Nulo'] += 1
    elif vote == 'Branco':
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
    sleep(1.5)
    print(f'  {winner[2][0]}!')
    sleep(0.5)
    print('tivemos', available['Bolsonaro'], 'votos para o bolsonaro')
    print('tivemos', available['Lula'], 'votos para o Lula')
    print('tivemos', available['Batman'], 'votos para o Batman')
    print('tivemos', unavailable['Nulo'], 'votos nulos')
    print('tivemos', unavailable['Branco'], 'votos em branco')


