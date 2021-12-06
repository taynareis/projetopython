'''Crie um programa que leia a idade e sexo de varias pessoas, a cada pessoa cadastrada, o programa
deverá perguntar se o usuario quer ou não continuar. No final mostra: Qts pessoas tem mais de 18 anos
Quantos homens foram cadastrados, Qts mulheres tem menos de 20 anos'''
total = homem = mulher = 0
while True:
    print('====CADASTRE A PESSOA====')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    if idade >= 18:
        total += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Total de Homens cadastrados: {homem}')
print(f'Total de Mulheres com menos de 20 anos: {mulher}')
