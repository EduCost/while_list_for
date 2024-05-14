# 4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
print("Digite 10 caracteres:")
contador = 1
while contador <= 10:
    letras.append(input(f'Caractere {contador}: ').lower())
    contador += 1

consoantes_lista = []
indice = 0
while indice < len(letras):
    if letras[indice] not in 'aeiou':
        consoantes_lista.append(letras[indice])
    indice += 1

print(f'Número de consoantes: {len(consoantes_lista)}')
print(f'Consoantes lidas: {consoantes_lista}')
