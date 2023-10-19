numeros = []

while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    else:
        numeros.append(numero)

print(numeros)

print('\nUsando reverse')
numeros.reverse()
print(numeros)
numeros.reverse() # pra voltar ao formato original

print('\nSem usar reverse')
tamanho = len(numeros)
contador = 1
numeros_reverso = []

for i in range(len(numeros)):
    numeros_reverso.append(numeros[tamanho - contador])
    contador += 1

print(numeros_reverso)
