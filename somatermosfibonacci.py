# Soma dos n termos da sequência Fibonacci       
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        a,b = b, b+a
    return a

soma = 0
n = int(input('Insira a quantidade de termos que deseja somar da sequência de Fibonacci:'))
for x in range(n):
    soma+=fibonacci(x)
print('A soma dos n termos da sequência de Fibonacci é de:', soma)