'''Crie um programa onde o usuario possa digitar cinco valores numéricos e cadastre os em uma lista já na posição correta ( sem utilizar sort).
No final mostre a lista ordenada na tela'''
lista = []
for v in range(0, 5):
    num = int(input('Digite um número: '))
    if v == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(f'Valores digitados em ordem: {lista}')


