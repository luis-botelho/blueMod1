#Eu fiz uma bagunça aqui, começei a fazer no pensamento "Não faz sentido eu pegar o voto de quem não tem idade para votar", resumo : acabei com 5 funções, como estou com pouco tempo para fazer exercícios foi bom quebrar a cabeça aqui para treinar, vou estudar mais!
from functions import autorizaVoto, votacao,result, winner
#Variável para continuar a receber votos até que digite não
condition = ""
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
    result(vote, candidates, null)
    condition = str(input('Tem mais alguém para votar ?\n').upper().replace(',','.'))
winner(candidates,null)