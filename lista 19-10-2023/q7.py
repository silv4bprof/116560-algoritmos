lista = []
for i in range(1, 21):
    print(i)
    lista.append(i)

# Jeito espeto
print(lista)

# Jeito legal
print("[", end='')
for i in range(len(lista)):
    if i == len(lista) - 1:
        print(lista[i], end='')
    else:
        print(lista[i], end=', ')
print("]")
