'''Crie um programa onde o usuario digite sete valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente'''
lista = [[], []]
for v in range(0, 7):
    num = int(input(f'Digite o {v + 1}° número: '))
    lista.append(num)
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
