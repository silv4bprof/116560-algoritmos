alunos = []

linhas = int(input('Quantidade de alunos: '))

for a in range(linhas):
    aluno = []
    print(f'Informações do aluno {a+1}:')
    matricula = int(input('Número da matrícula: '))
    media_provas = float(input('Média das provas: '))
    media_trabalhos = float(input('Média dos trabalhos: '))
    nota_final = (media_provas + media_trabalhos)/2
    print(f'Nota final: {nota_final:.2f}')

    aluno.append(matricula)
    aluno.append(media_provas)
    aluno.append(media_trabalhos)
    aluno.append(nota_final)
    alunos.append(aluno)


maior = 0
matricula_maior = 0

for l in range(len(alunos)):
    if alunos[l][-1] > maior:
        maior = alunos[l][-1]
        matricula_maior = alunos[l][0]

soma = media_turma = 0
for l in range(len(alunos)):
    soma += alunos[l][-1]

media_turma = soma / linhas

print(f'Matrícula do aluno com a maior nota final: {matricula_maior}')
print(f'Média aritmética das notas finais: {media_turma:.2f}, pois:', end=' ')


if len(alunos) > 1:
    for l in range(len(alunos)):
        print(f'{alunos[l][-1]} +', end=' ')
else:
    print(f'{alunos[l][-1]}', end=' ')

print(f'/ {linhas} = {media_turma:.2f}')
