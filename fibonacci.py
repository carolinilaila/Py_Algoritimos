## FIBONACCI - n termos
def fibonacci():
    a = 0
    b = 1
    cont = 0
    soma = 0
    while cont < n:
        print(a , end=' ')
        b = b+a
        a = b-a
        cont+=1
    
n = int(input('Insira a quantidade de termos que deseja conhecer da sequência Fibonacci: '))
if n > 0:
    fibonacci()
elif n == 0:
    print(0)