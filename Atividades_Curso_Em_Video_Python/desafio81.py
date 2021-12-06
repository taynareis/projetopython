'''Crie um programa que leia varios numeros e coloque em uma lista. depois disso mostre: A) Qts numeros foram digitados
B) A lista dos valores em ordem decrescente. C) Se o valor 5 foi digitado e está ou não na lista'''
valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'Foram digitados {len(valores)} valores.')
valores.reverse()
print(f'Os valores em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')


