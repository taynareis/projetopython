'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''
from random import randint
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
for j, n in jogo.items():
    print(f'{j} tirou o número: {n}.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('*-' * 20)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v}')
print('*-' * 20)
