# Crie um programa que leia um número qualquer e mostre se é par ou impar
num = int(input('Digite um número para saber se ele é PAR ou ÍMPAR: '))
resto = num % 2
if resto == 0:
    print('O número é PAR!')
else:
    print('O número é ÍMPAR!')
print('--FIM--')
