# Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre

# A - quantas pessoas tem mais de 18 anos
# B - Quantos Homens foram cadastrados
# C - Quantas mulheres tem menos de 20 anos.

maior_idade = homens = novinhas = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper()
    if sexo == 'F' and idade < 20:
        novinhas += 1
    if sexo == 'M':
        homens += 1
    if idade > 18:
        maior_idade += 1
    continua = int(input('\nContinua: \n[1] para sim \n[2] para não\n\n'))
    if continua == 2:
        break
print(f'Maior de 18 > {maior_idade}\nHomens cadastrados > {homens}\nNovinhas > {novinhas}')



