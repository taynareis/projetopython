''' refazer o exercicio 35 e acrescentar o recurso de mostrar o tipo de triangulo formado:
- equilátero: todos os lados iguais, - isósceles: dois lados iguais, - escaleno: todos os lados diferentes '''
n1 = float(input('primeiro segmento: '))
n2 = float(input('segundo segmento: '))
n3 = float(input('terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Essas retas formam um Triângulo.')
    if n1 == n2 == n3:
        print('O triângulo formado é EQUILÁTERO.')
    elif n1 != n2 != n3:
        print('O triângulo é ESCALENO.')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('O triângulo é ISÓSCELES.')
else:
    print('Essas retas não formam um Triângulo.')
