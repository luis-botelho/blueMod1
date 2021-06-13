#exercicios da aula 5
#Módulo de logica de programação
#1 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.Caso esteja errado,peça a digitação novamente até ter um valor correto.

sex = str(input('Qual seu sexo ? ').upper())
if sex == "M":
    print('Sexo masculino guardado com sucesso!')
elif sex == "F":
    print('Sexo feminino guardado com sucesso!')
else:
    while not sex == "F" or not sex == "M": 
        print('Sexo digitado não encontrado, digite novamente.')
        sex = str(input('Qual seu sexo ? ').upper())
        if sex == "M":
            print('Sexo masculino guardado com sucesso!')
            break
        elif sex == "F":
            print('Sexo feminino guardado com sucesso!')
            break
#2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem corretamente a senha. A senha é “Blue123” 
#2b - Exiba quantas vezes o usuário errou a digitação.

key = str(input('Digite a senha: '))
password = "Blue123"
try_ = 0
if key == password:
    print('Senha digitada correta!')
else:  
    while not key == password:
        try_ += 1
        print('Senha incorreta, tente novamente. ')
        key = str(input('Digite a senha: '))
        if key == password:
            print('Senha digitada correta!')
            print(try_)
            break
#3 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

#variáveis 
man = 0
teenWoman= 0 
try_ = 1
age = 0

var1 = str(input('Qual seu sexo? : ').upper())
var2 = int(input('Qual sua idade ? : ').upper())
var3 = str(input('Deseja continuar ? : ').upper().replace('Ã' , 'A'))
if var2 > 18:
    age += 1
if var1[0] == 'M':
    man += 1
if var1[0] == 'F' and var2 < 20:
    teenWoman += 1
while not var3 == 'NAO':
    var1 = str(input('Qual seu sexo? : ').upper())
    var2 = int(input('Qual sua idade ? : ').upper())
    var3 = str(input('Deseja continuar ? : ').upper().replace('Ã' , 'A'))    
    try_ += 1
    if var2 > 18:
      age += 1
    if var1[0] == 'M':
      man += 1
    if var1[0] == 'F' and var2 < 20:
      teenWoman += 1

print(f'Foram cadastradas {age} pessoa com mais de 18 anos' )
print(f'{man} homens cadastrados')
print(f'{teenWoman} mulheres com menos de 20 anos' )
print(f'Com um total de {try_} pessoas cadastradas')
#4 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random 

result = random.randint(0,10)
user = int(input('O programa vai pensar em um número de 0 a 10\nTente adivinhar este número\nResposta: '))
try_ = 1

while not result == user:
  print('Infelizmente você errou')
  user = int(input('Tente novamente\nResposta: '))
  try_ += 1
if result == user:
  print('Parabéns! Você acertou!')
print(f'Você tentou {try_} vezes')

