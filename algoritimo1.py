'''
Análise da Situação do Aluno

Programa que a partir da média, do número de aulas e faltas do aluno, defina seu resultado na disciplina. 
Os resultados possíveis são: APROVADO e REPROVADO. Para ser considerado APROVADO, 
o aluno precisa se enquadrar em uma das seguintes situações:

a) Frequência maior ou igual 75% com média maior ou igual a 5;

b) Frequência maior ou igual a 50% caso a média seja maior ou igual a 7.

Caso não se enquadre em pelo menos uma delas, é considerado REPROVADO.

'''

media,aulas,faltas = input().split(" Insira a média da sala, as aulas e as faltas do aluno: ")
media = float(media)
aulas = int(aulas)
faltas = int(faltas)
freq =  100 - ((faltas*100)/aulas)

if freq >= 75 and media >= 5:
    print('APROVADO')
elif freq >= 50 and media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')
print(freq)