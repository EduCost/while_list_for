# 9.Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

numeros = [2, 13, 17, 7, 11, 20, 8, 1, 22, 30]
soma_quadrados = 0
for n in numeros:
    soma_quadrados += n ** 2
print(f'A soma dos quadrados é de {soma_quadrados}')
