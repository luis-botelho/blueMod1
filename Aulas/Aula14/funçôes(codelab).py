# def soma(x,y,z):
#     resultado = x + y + z
#     return resultado
# num1 = int(input('Digite um número\n'))
# num2 = int(input('Digite um número\n'))
# num3 = int(input('Digite um número\n'))
# resultado = soma(num1,num2,num3)
# print(f'{resultado}')

# def salario(x,y):
#     salariobase = x*y #-->
#     salarioextra = 0
#     if y > 40:
#         salarioextra = (y-40)*1.5

#     return salarioextra + salariobase
   
# valorxhora = 10
# colaborador = float(input('Quantas horas você trabalhou?\n').replace(',','.'))
# print(salario(valorxhora,colaborador))

ano = int(input())
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano Bissexto")
else:
    print("Não é um ano Bissexto!")
