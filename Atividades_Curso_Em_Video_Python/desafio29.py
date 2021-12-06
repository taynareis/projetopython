# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostra mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada km acima do limite
v = float(input('Velocidade atual do carro: '))
if v > 80:
    print('Você foi multado, pois ultrapassou o limite de velocidade de 80km/h.')
    multa = (v-80) * 7
    print('O valor da multa é de: R$ {:.2f}'.format(multa))
    print('Tenha um bom dia. Dirija com segurança')
else:
    print('Tenha um bom dia. Dirija com segurança!')
print('--FIM--')
