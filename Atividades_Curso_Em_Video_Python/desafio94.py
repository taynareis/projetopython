
'''Crie um programa que leia nome, sexo e idade de vários pessoas, guarde os dados de cada um em um dicion´rio,
e todos os dicionários em uma lista. No final, mostre: A) Qts pessoas foram cadastradas, B) A média de idade do grupo
C)Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acim da média'''
dados = dict()
lista = list()
listamulher = list()
media = soma = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo:[F/M] '))
    dados['Idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    mais = str(input('Deseja continuar?[S/N] '))
    soma += dados['Idade']
    if dados['Sexo'] in 'Ff':
        listamulher.append(dados['Nome'])
    if mais in 'Nn':
        break
media = soma / len(lista)
print('=-' * 35)
print(f'A) Total de pessoas cadastradas: {len(lista)}')
print(f'B) Média de idade do Grupo: {media}')
print(f'C) Lista com todas as mulheres: {listamulher}')
print('=-' * 35)
for p in lista:
    if p['Idade'] >= media:
        print(f'D) Pessoas com idade acima da média: {p}', end=' ')
        print()
