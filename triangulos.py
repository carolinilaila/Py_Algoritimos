''' Insira 3 valores e descubra se pode formar um triângulo. '''

aresta1 = int(input('Insira o tamanho da aresta 1: '))
aresta2 = int(input('Insira o tamanho da aresta 2: '))
aresta3 = int(input('Insira o tamanho da aresta 3: '))

if aresta1 + aresta2 > aresta3 and aresta3 + aresta2 > aresta1 and aresta1 + aresta3 > aresta2:
    if aresta1 == aresta2 and aresta2 == aresta3:
        print('Pode formar um triangulo equilatero.')
    elif (aresta1 == aresta2 and aresta1 != aresta3) or (aresta2 == aresta3 and aresta2 != aresta1):
        print('Pode formar um triangulo isosceles.')
    elif aresta1 != aresta2 and aresta2 != aresta3 or aresta1 != aresta3:
        print('Pode formar um triangulo escaleno.')
else:
    print('Não pode formar um triangulo!')