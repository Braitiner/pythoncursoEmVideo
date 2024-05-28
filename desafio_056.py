# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

soma = 0
velho = int(0)
nome_velho = 'vazio'
novinha = 0
for i in range(0,4):
    nome = str(input('Nome: '))
    sexo = str(input('M / F: ')).upper()
    idade = int(input('Idade: '))
    soma += idade
    if sexo == 'M':
        print('primeiro if')
        if idade > velho:
            print('segundo if')
            velho = idade
            nome_velho = nome
    if sexo == 'F':
        if idade < 20:
            novinha += 1
media = soma/4
print('Media: {:.2f}\nHomem mais velho: {}\nNovinhas: {}'.format(media, nome_velho, novinha))