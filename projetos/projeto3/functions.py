
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



