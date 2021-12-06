'''Melhore o desafio 61, perguntando o usuario se el quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += razao
        cont += 1
    print('PAUSA...')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'A progressão foi finalizada com {total} termos.')
