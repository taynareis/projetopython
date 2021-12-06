'''Faça um progrma que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for a, s in aluno.items():
    print(f'{a} é igual a {s}.')
