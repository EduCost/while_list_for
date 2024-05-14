# 2.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

contagem = 1
numeros = []
while contagem <= 10:
    numeros.append(float(input(f'{contagem}º Número: ')))
    contagem += 1

inverso = 9
while inverso != 0:
    print(numeros[inverso])
    inverso -= 1