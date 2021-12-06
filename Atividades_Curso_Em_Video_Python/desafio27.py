# Faça um programa que leia o nome completo da pessoa e mostre o primeiro e o último nome
n = str(input('Digite seu nome completo: ')).upper().strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
