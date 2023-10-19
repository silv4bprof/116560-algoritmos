l_nome = []
l_sobrenome = []

nome = input('Nome: ')
sobrenome = input('Sobrenome: ')

for i in nome:
    l_nome.append(i)

for i in sobrenome:
    l_sobrenome.append(i)

print(l_nome, 'com', len(l_nome), 'letras')
print(l_sobrenome, 'com', len(l_sobrenome), 'letras')

print('\nSeu nome é:', (l_nome + l_sobrenome))

l_nome = ''.join(l_nome)
l_sobrenome = ''.join(l_sobrenome)

print('\nSeu nome é:', l_nome, l_sobrenome)