'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final mostre: A média de idade do grupo; Qual é o nome do homem mais velho;
Quantas mulheres tem menos de 20 anos'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------ {}° PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    mediaidade = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('Média de idade do grupo: {} anos'.format(mediaidade))
print('O homem mais velho é o {} e ele tem {} anos.'.format(nomevelho, maioridadehomem))
print('Mulheres com menos de 20 anos: {}'.format(totmulher20))
