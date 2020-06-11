'''
 FATORIAL

'''
a = int(input('Insira um número maior que zero: '))
n = a
if a > 0:
    for b in range (a-1,0,-1):
        a = a*b
    print('Fatorial de',n,'é:', a)
