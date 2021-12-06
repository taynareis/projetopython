'''Crie um programa que tenha função leiaInt, que vai funcionar de forma semelhante a função input do python,
só que fazendo a validação para aceitar apenas um valor numérico. ex) n = leiaint('Digite um num')'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro!Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
