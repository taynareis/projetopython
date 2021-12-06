'''Crie um programa que tenha uma função chamada voto que vai receber como parâmetro o ano de nascimento de uma pessoa
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições'''


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade < 65:
        print(f'A idade é {idade}, e o voto é Obrigatório.')
    elif idade < 16:
        print(f'A idade é {idade}, e o voto é Negado.')
    elif idade >= 16 or idade > 65:
        print(f'A idade é {idade}, e o voto é Opcional.')


ano = int(input('Ano de nascimento: '))
voto(ano)
