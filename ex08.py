# 8.Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range(1, 6):
    idades.append(int(input(f'Digite a idade da pessoa {i}: ')))
    alturas.append(float(input(f'Digite a altura da pessoa {i} em metros: ')))

print('Idades e alturas na ordem inversa:')
for i in range(4, -1, -1):
    print(f'Idade: {idades[i]} anos, Altura: {alturas[i]} metros')
