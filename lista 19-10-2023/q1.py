lista = []

while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    lista.append(numero)

for i in range(len(lista)):
    print(f'Elemento: {lista[i]} - Posição: {i}')
