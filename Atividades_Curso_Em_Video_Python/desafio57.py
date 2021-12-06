'''Faça um programa que leia o Sexo da pessoa, mas só aceite os valores
M ou F. Caso esteja errado, peça a digitação novamente
até ter um valor correto.'''
sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
    if sexo in 'MmFf':
        break
print('Sexo {} registrado com sucesso!'.format(sexo))