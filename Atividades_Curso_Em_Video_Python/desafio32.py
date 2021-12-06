# Faça um programa que leia um ano e mostre se ele é bissexto
ano = int(input('Digite um ano para saber se é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
print('---FIM---')
'''
if ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano digitado é bissexto')
    else:
        print('Elé é divisivel por 4, mas é divisivel por 100!')
else:
    print('O ano não é bissexto, porque não é divisivel por 4!')'''
