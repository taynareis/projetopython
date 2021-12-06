'''programa que calcule o valor a ser pago por um produto cosiderando o seu preço normal e condição de pagamento
a vista dinheiro/cheque: 10% de desconto; a vista no cartão: 5% de desconto; em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros'''
from time import sleep
valor = float(input('Qual é o preço normal do produto? '))
menu = 0
while menu != 5:
    print('''\033[4;34mFormas de pagamento:\033[m 
[1] A vista no dinheiro ou cheque 
[2] A vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão
[5] Sair do programa''')
    menu = int(input('\033[33mDigite o número correspondente a forma de pagamento desejada: \033[m'))
    if menu == 1:
        sleep(1)
        print('10% de DESCONTO para pagamento a vista!')
        print('O valor do produto com desconto é de: \033[32mR$ {}\033[m'.format(valor - (valor * 0.10)))
        print('Obrigado! Volte sempre!')
        break
    elif menu == 2:
        sleep(1)
        print('5% de DESCONTO para pagamento a vista no cartão!')
        print('O valor do produto com desconto é de: \033[32mR$ {}\033[m'.format(valor - (valor * 0.05)))
        print('Obrigado! Volte sempre!')
        break
    elif menu == 3:
        sleep(1)
        print('O valor do produto permanece o mesmo: \033[32mR$ {}\033[m'.format(valor))
        print('Obrigado! Volte sempre!')
        break
    elif menu == 4:
        sleep(1)
        print('Para pagamento em 3x ou mais no cartão, você terá um acréscimo de 20% de juros.')
        print('O valor do produto será: \033[32mR$ {}\033[m'.format(valor + (valor * 0.20)))
        print('Obrigado! Volte sempre!')
        break
    elif menu == 5:
        sleep(1)
        print('Você saiu do programa. Até mais, volte sempre!')
        break
    else:
        sleep(1)
        print('\033[31mValor digitado inválido. Por favor, digite novamente.\033[m')
