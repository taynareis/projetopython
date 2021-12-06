''' Escreva um programa que leia dois numeros inteiros e compare-os, mostrando uma mensagem na tela
- o primeiro valor é maior, - o segundo valor é maior, - não existe valor maior, os dois são iguais '''
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Não existe número maior, os dois são iguais!')
