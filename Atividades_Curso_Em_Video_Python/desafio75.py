'''Desenvolva um programa que leia quatro valores pelo teclado e guarde em uma tupla. No final mostre:
Qts vezes apareceu o valor 9 - Em que posição foi digitado o primeiro valor 3 - Quais foram os números pares'''
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
print(f'O valor 3 apareceu na {num.index(3) + 1}° posição.')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
