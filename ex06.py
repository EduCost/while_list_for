# 6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

media = []
contador = 1
while contador <= 3:
    print(f'{contador}º aluno')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    n4 = float(input('Nota 4: '))
    media.append((n1+n2+n3+n4) / 4)
    contador += 1

media7 = 0
for m in media:
    if m >= 7:
        media7 += 1
print(f'{media7} alunos estão com a média igual ou maior a 7!')  