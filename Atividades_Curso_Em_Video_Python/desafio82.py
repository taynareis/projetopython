'''Crie um programa que leia varios numeros e coloque em uma lista. Depois, crue duas listas extras que vão conter
valores pares e os valores impares. No final mostre o conteudo das tres listas geradas'''
lista1 = []
lista2 = []
lista3 = []
while True:
    num = int(input('Digite um número: '))
    lista1.append(num)
    continuar = str(input('Deseja continuar?[S/N] '))
    if continuar in 'Nn':
        break
for v in lista1:
    if v % 2 == 0:
        lista2.append(v)
    if v % 2 == 1:
        lista3.append(v)
print('=-' * 30)
print(f'Lista completa: {lista1}')
print(f'Lista números pares: {lista2}')
print(f'Lista números ímpares: {lista3}')
