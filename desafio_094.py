# Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
# No final mostre:
#A Quantas pessoas foram cadastradas
#B A media de idade do grupo.
#C Uma lista com todas as mulheres.
#D Uma lista com todas as pessoas com idade acima da media

lista = []
mulheres = []
acima = []
pessoa = {}
total_idade = 0
while True:
    pessoa.clear()
    pessoa = {'nome': input('Nome: '), 'sexo': str(input('Sexo [M/F]')), 'idade': int(input('Idade: '))}
    total_idade += pessoa['idade']
    if pessoa['sexo'] in 'fF':
        mulheres.append(pessoa['nome'])
    lista.append(pessoa.copy())
    parar = str(input('Deseja continuar [S/N]'))
    if parar in 'Nn':
        break
print(f'foram cadastradas {len(lista)}')
print(f'A media de idade do grupo é {total_idade/len(lista)}')
print(mulheres)
for v in lista:
    if v['idade'] > (total_idade/len(lista)):
        acima.append(v['nome'])
print(acima)

