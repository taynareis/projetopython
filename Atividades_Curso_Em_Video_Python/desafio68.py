'''Faça um programa que jogue par ou impar com o computador. O jogo só se encerra quando o jogador perder.
Motrando o total de vitórias consecutivas que ele conquistou.'''
from random import randint
cont = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    if tipo not in 'PI':
       tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total = {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            cont += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            cont += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!! Você venceu {cont} vezes.')
