'''Crie um programa que leia vários números inteiros, e só pare se o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e a soma entre eles.'''
num = 0
soma = num
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
print(f'A soma de todos os valores é igual a : {soma - 999}')
