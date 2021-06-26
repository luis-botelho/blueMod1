def autorizaVoto(year):
    if year < 16:
      return 'Negado'
    elif year >= 18 and year < 71:
      return 'Obrigatório'
    elif year < 16 or year > 70:
      return 'Opcional'
def votacao(validate):
    vote = 0
    if validate == 'Negado':
        print(f'Infelizmente Você ainda é muito novo para poder votar!')
        pass
    elif validate == 'Obrigatório':
        while vote > 5 or vote < 1:
            print('Escolha um dos candidatos no menu a abaixo:\n[1] Bolsonaro\n[2] Lula\n[3] Batman\n[4] Nulo\n[5] Voto em branco')
            vote = int(input('opção'))
    elif validate == 'Opcional':
        option = str(input('Seu voto não é obrigatório deseja votar ?\n').upper().strip())
        if option[0] == "S":
            while vote > 5 or vote < 1:
                print('Escolha um dos candidatos no menu a abaixo:\n[1] Bolsonaro\n[2] Lula\n[3] Batman\n[4] Nulo\n[5] Voto em branco')
                vote = int(input('opção'))
        elif option [0] == "N":
            pass
        else:
            print('Você digitou algo errado, voto cancelado!')          
    return vote
def apuracao(vote):
    #dict com os nomes dos candidatos
    candidates = {'Bolsonaro': 0, 'Lula': 0, 'Batman': 0}
    #dict com os votos em brancos (Depois de pequisar descobri que na verdade os votos nulos e em branco só servem para questões estatisticas)
    null = {'Nulo':0,'Branco':0}
    if vote == 1:
        candidates['Bolsonaro'] += 1
    elif vote == 2:
        candidates['Lula'] += 1
    elif vote == 3:
        candidates['Batman'] += 1
    elif vote == 4:
        null['Nulo'] += 1
    elif vote == 5:
        null['Branco'] += 1 
    result = list(candidates)
    print(result)




