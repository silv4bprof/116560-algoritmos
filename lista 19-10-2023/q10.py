lista = []
numero_unico = ''

while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    lista.append(str(numero))

for elemento in lista:
    numero_unico = numero_unico + elemento

print(numero_unico)
