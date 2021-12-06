'''Melhore o jogo do DESAFIO 28. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
computador = randint(0, 10) # Faz o computador "PENSAR"
print('\033[0;31m' + '-=-' * 20)
print('Vou pensar em número entre 0 e 10, tente advinhar...')
print('-=-' * 20 + ('\033[m'))
sleep(2)
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez...')
        elif jogador > computador:
            print('Menos... Tente outra vez...')
print('\033[0;35mPARABÉNS! Você conseguiu me vencer com {} tentativas!\033[m'.format(tentativa))

print('---FIM---')
