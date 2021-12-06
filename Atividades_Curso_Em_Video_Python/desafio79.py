'''Crie um programa onde o usuario possa digitar varios valores númericos e cadastre-os em uma lista
Caso o número já exista lá dentro, ele não será adicionado. No final, serao exibidos todos os valores unicos digitados em ordem crescente'''
valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
valores.sort()
print(f'Você digitou os valores: {valores}')
