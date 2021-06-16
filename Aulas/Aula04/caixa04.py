#Projeto da semana
#Caixa eletrônico

#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
#Código para facil manutenção
print('Qual a quantidade deseja sacar ?')
saque = int(input('R$ '))
#variáveis para a quantiade de notas 
quant1 = 0
quant2 = 0
quant3 = 0
quant4 = 0
quant5 = 0
#varáveis para o valor das notas
value1 = 100 
value2 = 50
value3 = 10
value4 = 5
value5 = 1
#Repetição caso o usuário digite um valor incorreto
while saque < 10 or saque > 600:
    print('Quantidade informada inválida, digite novamente')
    saque = int(input('R$ '))
#aux <- é a variavel que ajuda a não perder o valor que o usuário digitou.
aux = saque 
#começando das notas maiores para as menores fazendo a divisão inteira do valor do usuário, depois diminuindo ele pela quantidade de notas multiplicados pelo valor da nota.
quant1 = aux // value1
aux = aux - (quant1*value1)
#assim no próximo calculo o valor de aux é igual a o oque restou do primeiro calculo. 
quant2 = aux // value2
aux = aux - (quant2*value2)

quant3 = aux // value3
aux = aux - (quant3*value3)

quant4 = aux // value4
aux = aux - (quant4*value4)

quant5 = aux // value5
aux = aux - (quant5*value5)

print(f'Para sacar a quantia de R${saque}, você vai precisar de: ')
#Se a quantidade de notas forem menores que 1, o usuário não vai ver o print referente a ela.
if quant1 > 0:
    print(f'{quant1} notas de R$ {value1}')
if quant2 > 0:
    print(f'{quant2} notas de R$ {value2}')
if quant3 > 0:
    print(f'{quant3} notas de R$ {value3}')
if quant4 > 0:
    print(f'{quant4} notas de R$ {value4}')
if quant5 > 0:
    print(f'{quant5} notas de R$ {value5}')