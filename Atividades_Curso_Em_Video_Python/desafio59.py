'''Crie um programa que leia dois valores e mostre um menu na tela:
[1]Somar [2] multiplicar [3] maior [4]novos números [5]Sair do programa,
Seu programa deverá realizar a operação solicitada em cada caso'''
from time import sleep
lista = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while lista != 5:
    sleep(1)
    lista = int(input('''\033[35;1mEscolha uma opção:
    \033[34;1m[1]Somar 
    [2] multiplicar 
    [3] maior 
    [4]novos números 
    [5]Sair do programa
    \033[35mDigite a opção desejada:\033[m '''))
    sleep(1)
    if lista == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    if lista == 2:
        multip = n1 * n2
        print('A multiplicação de {} x {} = {}'.format(n1, n2, multip))
    if lista == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1, n2))
        if n2 > n1:
            print('O número {} é maior que o número {}'.format(n2, n1))
    if lista == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
print('Você saiu do programa.')
