# 5.Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

contador = 1
pares = []
impares = []
while contador <= 20:
    num = int(input(f'{contador}º Número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    contador += 1
print(f'Os números pares digitados foram: {pares}')
print(f'Os números impares digitados foram: {impares}')