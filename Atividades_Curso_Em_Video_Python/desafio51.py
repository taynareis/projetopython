'''Desenvolva que leia o primeiro termo e a razao de um PA.
No final mostre os 10 primeiros termos dessa progressão'''
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (11-1) * razao
for pa in range(termo, decimo, razao):
    print(f'{pa}', end=' -> ')
print('Acabou!')