numeros = []

while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    else:
        numeros.append(numero)

maior = numeros[0]
menor = numeros[0]

for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]

for j in range(len(numeros)):
    if numeros[j] < menor:
        menor = numeros[j]

print('Maior:', maior)
print('Menor:', menor)