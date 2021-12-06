'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições.'''
valores = list()
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um número na posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Você digitou os números: {valores}')
print(f'O maior valor digitado foi: {max(valores)} e está na posição ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}... ', end='')
print()
print(f'O menor valor digitado foi: {min(valores)} e está na posição ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}... ', end='')
print()




