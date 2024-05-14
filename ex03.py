# 3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

contagem = 1
notas = []
while contagem <= 4:
    notas.append(float(input(f'{contagem}º Nota: ')))
    contagem += 1
media = sum(notas) / 4
print(f'As notas foram {notas} e a média foi de {media}')    