'''Crie um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
até 9 anos: MIRIM, até 14 anos: INFANTIL, até 19 anos: JUNIOR, até 20 anos: SENIOR, acima: MASTER'''
from datetime import date
print('\033[4;34mSaiba em qual categoria você entra!!\033[m')
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria MIRIM.')
elif idade <= 14:
    print('Categoria INFANTIL.')
elif idade <= 19:
    print('Categoria JÚNIOR.')
elif idade <= 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER.')
