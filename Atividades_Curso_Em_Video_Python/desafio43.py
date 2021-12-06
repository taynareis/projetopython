'''Programa que leia o peso e a altura, calcule seu IMC e mostre seu status:
- abaixo de 18.5: abaixo do peso; - entre 18.5 e 25: peso ideal; - de 25 até 30: sobrepeso
- 30 até 40: obesidade, - acima de 40: obesidade mórbida'''
peso = float(input('Quanto você pesa? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('IMC {:.2f}: Abaixo do Peso'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC {:.2f}: Peso Ideal'.format(imc))
elif 25 <= imc < 30:
    print('IMC {:.2f}: Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('IMC {:.2f}: Obesidade'.format(imc))
else:
    print('IMC {:.2f}: Obesidade Mórbida'.format(imc))




