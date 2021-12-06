# Faça um programa que leia sum num de 0 a 9999 e mostre na tela os digitos separados
# ex: Digite um num: 1834 \n unidade: 4\n dezena: 3\n centena: 8\n milhar: 1
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
