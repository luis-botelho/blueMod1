#Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue pedra, papel e tesoura (Jokenpô) com você. O programa tem que:
#• Permitir que eu decida quantas rodadas iremos fazer;
#• Ler a minha escolha (Pedra, papel ou tesoura);
#• Decidir de forma aleatória a decisão do computador;
#• Mostrar quantas rodadas cada jogador ganhou;
#• Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um (computador e jogador);
#• Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, se não finalize o programa.
print('============================================================================================================')
print('                                        Jokenpô by: Luis-Botelho                                            ')
print('============================================================================================================')
print('Bem vindo(a) ao game Jokenpô\n escolha entre Pedra, papel ou tesoura e veja se consegue ganhar do computador.')
from random import randint
from time import sleep
computer = randint(1,3)
select = ["Pedra","Papel","Tesoura"]
loss = 0
win = 0
draw = 0
condition = 0

while condition != 'NAO':
    init = int(input('Quantas vezes quer jogar ?\n'))
    print(f'Sua partida será uma melhor de {init}')
    print('============================================================================================================')
    sleep(1)
    for i in range(init):
        computer = randint(1,3)
        print('============================================================================================================')
        user = int(input('Qual sua escolha ?\nDigite:\n[1] Para Pedra\n[2] Para Papel\n[3] para Tesoura\n').upper())
        print()
        sleep(0.5)
        print("JO\n")
        sleep(0.5)
        print("KEN\n")
        sleep(0.5)
        print("POOH!!!\n")
        print('============================================================================================================')
        print(f'Você escolheu {select[user - 1]}')
        print(f'O computador escolheu {select[computer - 1]}')
        sleep(0.7)
        if computer == 1:
            if user == 1:
                print('Deu empate')
                draw += 1
            elif user == 2:
                print('Você ganhou!')
                win += 1
            elif user == 3:
                print('Você perdeu')
                loss += 1
            
            else:
                print('Opção invalida')
                pass
            sleep(1)
        if computer == 2:
            if user == 2:
                print('Deu empate')
                draw += 1
            elif user == 3:
                print('Você ganhou!')
                win += 1
            elif user == 1:
                print('Você perdeu')
                loss += 1
            else:
                print('Opção invalida')
                pass
            sleep(1)
        if computer == 3:
            if user == 3:
                print('Deu empate')
                draw += 1
            elif user == 1:
                print('Você ganhou!')
                win += 1
            elif user == 2:
                print('Você perdeu')
                loss += 1
            else:
                print('Opção invalida')
                pass
            sleep(1)
    print('============================================================================================================')
    
    print(f'Você ganhou {win} vezes')
    sleep(1)
    print(f'O computador ganhou {loss} vezes')
    sleep(1)
    print(f'E tiveram {draw} empates')
    print('============================================================================================================')
    sleep(1)
    if win > loss:
        print('Parabéns! Você é o campeão!')
        print('============================================================================================================')
    elif loss > win:
        print('Não foi desta vez! O computador é o campeão.')
        print('============================================================================================================')
    else:
        print('Deu empate!')
        print('============================================================================================================')
    condition = str(input('Deseja jogar novamente ?\n').upper().replace('Ã' , 'A'))
