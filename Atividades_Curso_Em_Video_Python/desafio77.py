'''Crie um programa que tenha uma tupla com várias palavras, depois deve mostrar, para cada palavra,
quais são suas vogais.'''
palavras = ('hoje', 'amanha', 'programar', 'python', 'tupla', 'java')
print('VOGAIS')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
