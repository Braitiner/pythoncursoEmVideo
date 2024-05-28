# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionario. No final, mostre o conteúdo da estrutura na tela.

aluno = {'Nome':input('Nome:')}
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação']= 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')