nomes = []

while True:
    nome = input('Nome (pare) para parar: ')
    if nome == 'pare':
        break
    nomes.append(nome)

print('Primeiro nome cadastrado:', nomes[0])
print('ultimo nome cadastrado:', nomes[len(nomes) - 1])

if len(nomes) % 2 == 0:
    print('Não tem meio')
else:
    meio = ((len(nomes) - 1) / 2) + 1 
    print('Nome do meio:', nomes[int(meio)])