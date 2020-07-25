# Lendo valores inteiros e guardando em um vetor para mostrar no final o menor valor lido
num = []
maior = 0
menor = 0
print('Insira dez números e descubra qual é o menor dentre eles!')
for c in range(0,10):
    num.append(int(input('Insira um número: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
           menor = num[c]
print('O menor valor digitado é de:',menor)