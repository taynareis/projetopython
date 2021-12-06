# Desenvolva um programa que leia o comprimento de três retas
# e diga se elas podem ou não formar um triangulo
n1 = float(input('primeiro segmento: '))
n2 = float(input('segundo segmento: '))
n3 = float(input('terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Essas retas formam um Triângulo')
else:
    print('Essas retas não formam um Triângulo')
