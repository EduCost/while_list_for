# 7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = [4, 12, 8, 1, 17]
mult = 1
for n in vetor:
    mult *= n
print(f'Os números são {vetor}')
print(f'A soma é de {sum(vetor)}')
print(f'Multiplicando esse números é igual a {mult}')
