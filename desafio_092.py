# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso o CTPS for diferente de zero, 
# o dicionario receberá também o ano de contratação e o salario. Calcule e acreescente, alem da idade, com quantos anos a pessoa vai de aposentar.
from datetime import datetime
trabalhador = {'Nome': input('Nome: ')}
trabalhador['idade'] = datetime.now().year - int(input('Ano de Nacimento: '))
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('salario: R$ '))
    trabalhador['aposentadoria'] = ((trabalhador['contratacao'] + 35) - datetime.now().year) + trabalhador['idade']
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
