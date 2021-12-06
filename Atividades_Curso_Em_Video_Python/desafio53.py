'''Faça um programa que leia uma frase qualquer e diga se ela é um palíndromo
desconsiderando os espaços'''
frase = input('digite uma frase: ')
if frase.replace(' ', '') == frase[::-1].replace(' ', ''):
    print('eh palindromo')
else:
    print('num eh palindromo')
