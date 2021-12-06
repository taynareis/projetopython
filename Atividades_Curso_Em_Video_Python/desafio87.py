'''Aprimore o desafio anterior mostrando no final: A) A soma de todos os valores pares digitados. B) A soma
dos valores da terceira coluna. C) O maior valor da segunda linha'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

par = tcol = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('*=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
    print()
print('*=' * 30)
print(f'A soma dos valores pares é igual a {par}')
for linha in range(0, 3):
    tcol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é igual a: {tcol}')
for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é: {maior}')
