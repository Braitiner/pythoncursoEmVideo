# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro aluno se mostre a ordem sorteada

import random
nomes = ['Ana', 'João', 'Maria', 'Pedro']
tamanhoLista = len(nomes)
for i in range(tamanhoLista):
    aluno = random.randrange(0, tamanhoLista)
    print('Aluno: {}'.format(nomes[aluno]))
    nomes.pop(aluno)
    tamanhoLista = len(nomes)
