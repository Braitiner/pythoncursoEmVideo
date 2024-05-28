# A Confederação NAcional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SENIOR
#Acimas: MASTER

from datetime import datetime

ano = int(input('ano nascimento: '))
idade = datetime.now().year - ano

if idade <= 9:
    print('Mirin')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade == 20:
    print('Senior')
else:
    print('Master')
