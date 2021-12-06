# Desenvolva um programa que pergunte a distância de uma viagem em km
# Calcule o preço da passagem cobrando 0.50 por km para viagens de até 200km e
# 0.45 para viagens mais longas
d = float(input('Qual é a distância da viagem em km? '))
'''c = d * 0.50
l = d * 0.45
if d <= 200:
    print('Sua viagem ficará em R$ {:.2f}'.format(c))
else:
    print('Sua viagem ficará em R$ {:.2f}'.format(l))'''
preco = d * 0.50 if d <= 200 else d * 0.45
print('Sua viagem ficará em R$ {:.2f}'.format(preco))

