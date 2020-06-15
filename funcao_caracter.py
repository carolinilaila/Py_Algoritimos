''' Função que retorna a quantidade de caracteres que se repetem em uma string.'''

def caracteres(s,c):
    cont = 0
    for i in range (len(s)):
        if c == s[i]:
            cont+=1  
    return cont

s = str(input('Digite uma frase: '))
c = str(input('Digite uma letra: ')) 
f = caracteres(s,c)
print('A quantidade de caracteres que se repetem na frase é de:',f ,'vezes.')