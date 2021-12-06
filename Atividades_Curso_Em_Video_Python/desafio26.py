# Faça um programa que leia uma frase e mostre: Qts vezes aparece a letra 'A'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece pela última vez
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição: {}'.format(frase.rfind('A')+1))
