'''Faça um programa que leia nome e peso de várias pessoas guarde em uma lista, Mostre: A) Quantas pessoas foram
cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoa mais leves'''
dados = list()
pessoas = list()
pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    mais = str(input('Quer continuar? [S/N] '))
    pessoas.append(dados[:])
    dados.clear()
    if mais in 'Nn':
        break
print('=*' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi {pesado}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesado:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso cadastrado foi {leve}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'[{p[0]}] ', end='')
print()
