menu = """
Escolha o que fazer.
1. Adicionar caixa.
2. Remover caixa.
3. Exibir pilhas.
4. Sair.
"""
deposito = []

pilhas = int(input('Quantidade de fileiras: '))

for l in range(pilhas):
    deposito.append([])

while True:
    print(menu)
    opcao = int(input('opção: '))

    if opcao == 1:
        pos_fileira = int(
            input(f'Em qual fileira deseja adicionar (1 - {pilhas}): '))
        deposito[pos_fileira - 1].append('caixa')
        print('Caixa adicionada com sucesso!')
    elif opcao == 2:
        pos_fileira = int(
            input(f'De qual fileira deseja remover (1 - {pilhas}): '))
        deposito[pos_fileira - 1].pop()
        print('Caixa removida com sucesso!')
    elif opcao == 3:
        print('Exibindo pilhas do depósito\n')
        for i in range(len(deposito)):
            print(f'Pilha {i+1}:', end=' ')
            for elemento in deposito[i]:
                print(elemento, end=' ')
            print()
    elif opcao == 4:
        print('Saindo ...')
        break
    else:
        print('Inválido, tente novamente.')
