# 1.a) Crie uma classe pessoa com os seguintes atributos: nome, sobrenome e idade.
# 1.b) Acrescente a classe criada um método para mostrar os dados de uma pessoa.
# 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e métodos.



# class Pessoal():
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade
#     def show(self):
#         print(self.nome)
#         print(self.sobrenome)
#         print(self.idade)
# name = str(input('Digite seu nome: '))
# lastName = str(input('Digite seu sobrenome: '))
# age = int(input('Digite sua idade: '))
# person = Pessoal(name, lastName, age)
# person.show()
# 2) Crie uma classe chamada Conta para simular as operações de
# uma conta corrente. Sua classe deverá ter os atributos Titular e
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
# Conta e teste os atributos e métodos implementados.
from random import randint
class Conta():
    def __init__(self, titular , saldo):
        self.titular = titular
        self.saldo = saldo
    def Saldo(self):
        print(f'Seu saldo é de {self.saldo}')
    def Sacar(self, valor):
        self.saldo -= valor
    def Depositar(self, valor):
        self.saldo += valor
nome = str(input('Digite o nome de usúario: '))
conta = float(randint(125,3666))
cliente = Conta(nome,conta)
cliente.Saldo()
operator = int(input('Escolha uma operação :\nDIgite [1] para sacar\nDigite [2] para depositar \n:'))
if operator == 1:
    valor = int(input('Quanto deseja sacar ?:\n'))
    cliente.Sacar(valor)

elif operator == 2:
    valor = int(input('Quanto deseja sacar ?:\n'))
    cliente.Depositar(valor)
cliente.Saldo()