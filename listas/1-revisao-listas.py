lista = [1, 2, 43, 565, 63, 6]

# ordem reversa
print(lista[::-1])

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

# for i in range(0, len(lista)):
#     lista[i] = 'Wendell'

for i in range(0, len(lista)):
    print(f'Elemento -> {lista[i]}')

for elemento in lista:
    print(f'Elemento: {elemento}')

contador = 0
while contador < len(lista):
    print(lista[contador])
    contador = contador + 1  # contador += 1

# ============================================================

lista = [1, 2, 43, 565, 565, 63, 6]
lista.append('Bruno')  # adicionar valores na lista
print(lista)

# lista.pop();
# print(lista)

lista.remove(565)
print(lista)

numero = lista.index(565)
print(numero)

print('bruno')
lista = [1]
lista[0]

# ============================================================

lista.sort()
print(lista)

lista.sort()
lista.reverse()
# lista.sort(reverse=True)
print(lista)

print(max(lista))
print(min(lista))

# ============================================================

lista = [-5, 1, 2, 43, 565, -89, 565, 63, 6]

maior = lista[0]
menor = lista[0]

for i in lista:
    if maior > i:
        maior = i
    if menor < i:
        menor = i

print(f'Maior: {maior}\nMenor: {menor}')

crud = []
while True:
    nome = input('Nome: ').strip()
    if nome == '0':
        break
    crud.append(nome)

# print('\n--- Nomes digitados ---')
# for elemento in crud:
#     print(f'Indice: {crud.index(elemento)} Nome: {elemento}')

while True:
    print('\n--- Nomes digitados ---')
    for elemento in crud:
        print(f'Indice: {crud.index(elemento)} Nome: {elemento}')
    numero = int(
        input('Digite a posição do nome p/ remover (num negativo p sair): '))
    if numero < 0:
        break
    else:
        crud.pop(numero)
    continuar = input('Deseja remover mais? (s/n): ')
    if continuar == 'n':
        break

print('\n--- Nomes digitados ---')
for elemento in crud:
    print(f'Indice: {crud.index(elemento)} Nome: {elemento}')
