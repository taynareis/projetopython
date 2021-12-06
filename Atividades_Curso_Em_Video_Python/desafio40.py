'''Crie um programa que leia duas notas e calcule a média, mostrando uma mensagem no final de acordo
com a média atingida. - Média abaixo de 5.0: REPROVADO; - Media entre 5.0 e 6.9: RECUPERAçÃO;
- Média 7.0 ou superior: APROVADO'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
