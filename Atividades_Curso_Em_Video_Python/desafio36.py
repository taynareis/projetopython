''' Escreva um programa para aprovar um crédito bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário e quantos anos vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então empréstimo negado '''
print('\033[4;34mSimulação de Crédito Bancário\033[m')
valor = float(input('Qual é o valor do imóvel que será adquirido?R$ '))
salario = float(input('Qual é o seu salário?R$ '))
anos = float(input('Em quantos anos deseja pagar o empéstimo? '))
prest = valor / (12 * anos)
if prest < (0.30 * salario):
    print('\033[0;32mO valor da prestação mensal será:\033[34m R$ {:.2f}\033[m'.format(prest))
else:
    print('\033[0;31mEmpréstimo negado pois a prestação excede o limite de 30% da sua renda mensal!\033[m')
