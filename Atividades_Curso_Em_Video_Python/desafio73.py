'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabelo do Campeonato de Futebol, na ordem de colocação.
Depois mostre: A - Apenas os 5 primeiros colocados, b - Os ultimos 4 colocados, c - uma lista com os times em ordem alfabetica
d - em que posição está o time Chapecoense.'''
tabela = ('Atlético MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
          'Atlético PR', 'Internacional', 'Fluminense', 'América Mg', 'Atlético GO', 'Cuiabá',
          'Ceará SC', 'São Paulo', 'Juventude', 'Santos', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times: {tabela}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados são: {tabela[16:]}')
print('-=' * 15)
print('A tabela em ordem alfabética: ', sorted(tabela))
print('-=' * 15)
print(f'O time Chapecoense está na {(tabela.index("Chapecoense") + 1)}° posição')
print('-=' * 15)

