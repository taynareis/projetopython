'''Crie um programa que leia nome e DUAS notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente'''
cadastro = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('=*' * 24)
print('BOLETIM DE NOTAS')
print('-=' * 24)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    aluno = int(input('Mostrar nota de qual aluno? [999 interrompe] '))
    if aluno == 999:
        break
    if aluno <= len(cadastro) - 1:
        print(f'Notas de {cadastro[aluno][0]} são {cadastro[aluno][1]}')
print('<<<< VOLTE SEMPRE >>>>')
