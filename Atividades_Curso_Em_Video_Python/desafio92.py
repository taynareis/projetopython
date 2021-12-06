''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho. Cadastre-os (com idade) em um
dicionário. Se por acaso a CTPS for diferente de zero o dicionário recebe também o Ano de conratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import date
from time import sleep
nasc = date.today().year
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Ano de nascimento'] = int(input('Ano do nascimento: '))
dados['Idade'] = nasc - dados.get('Ano de nascimento')
dados['No. CTPS'] = int(input('Número Carteira de Trabalho: [digite 0 se não tiver] '))
if dados['No. CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Idade de Aposentadoria'] = (dados.get('Ano de contratação') - dados.get('Ano de nascimento')) + 35
print('*-' * 30)
for i, d in dados.items():
    sleep(1)
    print(f'{i} é: {d}')
