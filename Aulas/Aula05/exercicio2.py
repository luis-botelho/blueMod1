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