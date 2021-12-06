'''Faça um programa que leia um numero inteiro e diga se ele é ou não um
numero primo'''
num = int(input("Digite um número: "))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
print(f"O número {num} foi divisível {cont} vezes!")
if cont == 2:
    print("O número é primo")
else:
    print("O número não é primo")
