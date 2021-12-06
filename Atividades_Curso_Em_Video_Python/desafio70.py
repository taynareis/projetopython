'''Crie um programa que leia o nome e o preço de vários produtos. Ele deverá perguntar se o usuário vai continuar.
No final, mostre: Total gasto na compra, Qts produtos custam mais de R$1000, Qual é o nome do produto mais barato'''
total = cont = totmil = menor = 0
nomebarato = ''
while True:
    print('===CADASTRE O PRODUTO===')
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: R$  '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            nomebarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar cadastrando? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total gasto na compra: {total}')
print(f'Número de produtos que custam mais de R$1000: {totmil}')
print(f'Nome do produto mais barato: {nomebarato}')
print('===FIM DO PROGRAMA DE CADASTRO===')