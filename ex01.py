# 1.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

contagem = 1
numeros = []
while contagem <= 5:
    numeros.append(int(input(f'{contagem}º Número: ')))
    contagem += 1
print(numeros)
    