# Faça um programa que leia 3 numeros e mostre qual á o maior e o menor
a = int(input('primeiro número: '))
b = int(input('segundo número: '))
c = int(input('terceiro número: '))
lista = [a, b, c]
print('O maior valor digitado foi: {}.'.format(max(lista)))
print('O menor valor digitado foi: {}.'.format(min(lista)))
'''menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi: {}.'.format(menor))
print('O maior valor digitado foi: {}.'.format(maior))
'''
