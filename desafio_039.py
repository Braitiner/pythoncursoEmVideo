# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade?
#Se ele ainda vai se alistar no serviço militar
# Se é a hora de se alistar 
# Se ja passou do tempo de alistamento

# Seu programa tambem devera mostrar o tempo que falta ou que pasou do prazo.


from datetime import datetime

ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano

if idade < 18:
    print('Você tem {} anos de idade, Ainda falta {} anos para o alistamento'.format(idade, 18-idade))
elif idade == 18:
    print('Você tem {} anos de idade, está no tempo certo de realizar o alistamento'.format(idade))
if idade > 18:
    print('Você tem {} anos de idade, passou {} anos para o alistamento'.format(idade, idade-18))
