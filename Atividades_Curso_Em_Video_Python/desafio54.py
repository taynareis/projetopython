'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas já são maiores'''
from datetime import date
cont = 0
cont2 = 0
anoatual = date.today().year
for n in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    idade = anoatual - ano
    if idade < 18:
        cont += 1
    elif idade > 18:
         cont2 += 1
print('Número de pessoas que NÃO atingiram a maioridade: {}'.format(cont))
print('Número de pessoas que atingiram a maioridade: {}'.format(cont2))

