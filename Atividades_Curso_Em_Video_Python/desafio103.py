'''Faça um programa que tenha uma função chamada ficha, que receba dois parâmetros: nome de um jogador e qts gols marcou
o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente'''


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} marcou {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)




