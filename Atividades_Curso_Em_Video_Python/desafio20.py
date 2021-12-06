# O mesmo professor quer sortear a ordem de aprensentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro e mostre a ordem sorteada.
import random
a1 = str(input('aluno 1: '))
a2 = str(input('aluno 2: '))
a3 = str(input('aluno 3: '))
a4 = str(input('aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
