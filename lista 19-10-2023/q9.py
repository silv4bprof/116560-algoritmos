# numero = input('Numero: ')
# numero_str = str(numero)


# numero_invertido_str = numero_str[::-1]
# print('String: ', numero_invertido_str)


# numero_invertido = int(numero_invertido_str)
# print('Inteiro: ',numero_invertido)


# resultado = numero_invertido + 1000
# print(f"Resultado: {resultado}")

# ===========

numero = input('Numero: ')
numero_str = str(numero)

print('\nSem usar reverse')
tamanho = len(numero)
contador = 1
numeros_reverso = ''

for i in range(len(numero)):
    numeros_reverso += numero[tamanho - contador]
    contador += 1

print(numeros_reverso)
