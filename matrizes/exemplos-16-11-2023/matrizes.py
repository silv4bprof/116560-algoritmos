from random import randint

matriz = []  # lista

linha = int(input('Dimensão da linha: '))
coluna = int(input('Dimensão da coluna: '))

# Matriz base
print('\nMatriz Base:'.upper())
for l in range(linha):  # linha
    linha_gerada = [0] * coluna  # -> [0, 0, 0] # coluna
    print(f'{l+1}ª linha gerada: {linha_gerada}')
    matriz.append(linha_gerada)

# Exibir
print('\nExibindo Matriz:'.upper())
for l in range(linha):
    for c in range(coluna):
        print(matriz[l][c], end=' ')
    print()

# Preenchendo matriz
print('\nPreenchendo Matriz:'.upper())
for l in range(linha):
    for c in range(coluna):
        # matriz[l][c] = int(input(f'Número da posição [{l}][{c}]: '))
        matriz[l][c] = randint(0, 9)

# Exibir
print('\nExibindo Novamente Matriz:'.upper())
for l in range(linha):
    for c in range(coluna):
        print(matriz[l][c], end=' ')
    print()

print('\nPesquisando valor na Matriz:'.upper())
valor = int(input('Valor para pesquisa: '))
encontrei = False
for l in range(linha):
    for c in range(coluna):
        if valor in matriz[l]:
            encontrei = True

if encontrei:  # if encontrei = True
    print(f'O valor {valor} existe na lista!')
