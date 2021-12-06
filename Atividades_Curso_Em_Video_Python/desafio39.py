''' Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar; - Se é a hora de se alistar; - Se já passou do tempo de alistamento
O programa também deve mostrar o tempo que falta ou que passou do prazo '''
from datetime import date
ano = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - ano
if idade < 18:
    print('Você não tem idade para se alistar. Faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Chegou a hora de se alistar!')
else:
    print('Você passou do prazo para alistamento. Está {} anos atrasado.'.format(idade - 18))
