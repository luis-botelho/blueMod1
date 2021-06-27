# Projeto 03 – Simulador de Votação
# Crie um programa que simule um sistema de votação, ele deve receber votos até que o usuário diga que não tem mais ninguém para votar, esse programa
# precisa ter duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições. 
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá da função autoriza_voto()) e o voto que é o número que a pessoa votou. Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o contrário a 2° função deve validar o número que a pessoa escolheu, ela pode escolher de 1 a 5 (crie 3 candidatos para a votação):
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.
#porfessor, desculpe mas fiz 3 funções, porque não vi sentindo na pessoa votar depois validar ou não o voto baseado na idade, me atrapalhou na lógica, espero não perder ponto por isso lol, alem disso o código ficou mais bonitinho e estruturado ^-^
from functions import autorizaVoto, votacao, apuracao
condition = ""
decision = {}
#dict com os nomes dos candidatos
candidates = {'Bolsonaro': 0, 'Lula': 0, 'Batman': 0}
#dict com os votos em brancos (Depois de pequisar descobri que na verdade os votos nulos e em branco só servem para questões estatisticas)
null = {'Nulo':0,'Branco':0}
#Apresentação 
print('====================================================================================================\n                                  Votação para presidente 2022\n====================================================================================================')
print('Bem vindo(a) as eleições 2022')
#Começa o programa perguntando o nome para uma saldação amistosa.
while condition != "NAO":
    name = str(input('Qual é seu nome ?\n').title().strip())
    year = int(input(f'Olá {name}, em qual ano Você nasceu ?\n'))
    age = 2021 - year
    vote = votacao(autorizaVoto(age))

    if apuracao(vote) == 'Bolsonaro':
        candidates['Bolsonaro'] += 1
    elif apuracao(vote)== 'Lula':
        candidates['Lula'] += 1
    elif apuracao(vote)== 'Batman':
        candidates['Batman'] += 1
    elif apuracao(vote)=='Nulo':
        null['Nulo'] += 1
    elif apuracao(vote)== 'Branco':
        null['Branco'] += 1
    
    condition = str(input('Tem mais alguém para votar ?\n').upper().replace(',','.'))
print(candidates, null)


