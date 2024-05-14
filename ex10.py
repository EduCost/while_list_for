# 10.Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = [1, 17, 42, 8, 33, 25, 10, 49, 5, 22]
vetor2 = [36, 3, 19, 45, 7, 31, 14, 48, 2, 40]
vetor3 = []
for n in range(10):
    vetor3.append(vetor1[n])
    vetor3.append(vetor2[n])
print(vetor3)