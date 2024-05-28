# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
temp = []
temp_notas = []

while True:
    temp.append(str(input('Nome: ')))
    temp_notas.append(float(input('Nota 1: ')))
    temp_notas.append(float(input('Nota 2: ')))
    temp.append(temp_notas[:])
    alunos.append(temp[:])
    temp_notas.clear()
    temp.clear()
    if str(input('Quer continuar? [S/N]')) in 'Nn':
        break
print('No.      Nome               Média')
for i, a in enumerate(alunos):
    print(f'{i+1:<2}       {a[0]:<10}         {(sum(a[1]))/2:<3}')
while True:
    aluno = int(input('Mostrar notas de qual aluno:  (999 interromper)'))-1
    if aluno == 998:
        print('Fim do programa')
        break
    elif aluno < 0 or aluno > len(alunos):
        print('Opção invalida')
    else:
        print(f'Notas de {alunos[aluno][0]} são {alunos[aluno][1]}')