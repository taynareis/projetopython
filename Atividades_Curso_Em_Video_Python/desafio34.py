# escreva o programa que pergunte o salario e calcule o valor de seu aumento
# Para salários superiores a 1.250,00, aumento de 10%
# Para inferioes ou iguais, 15% de aumento
salario = float(input('Qual é o seu salário atual? '))
'''aumento = salario + (0.10 * salario) if salario > 1250 else salario + (0.15 * salario)
print('Salário atualizado: R$ {:.2f}'.format(aumento))'''
if salario > 1250:
    print('Seu salário é maior que R$ 1250')
    print('Seu aumento será de 10%')
    aumento = salario + (0.10 * salario)
    print('Salário atualizado: R$ {:.2f}'.format(aumento))
else:
    print('Seu salário é menor ou igual a R$ 1250')
    print('Seu aumento será de 15%')
    aumento = salario + (0.15 * salario)
    print('Salário atualizado: R$ {:.2f}'.format(aumento))
