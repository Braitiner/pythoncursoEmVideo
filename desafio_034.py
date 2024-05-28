# Escreva um progama que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Para salários superiores a R$1.737,50 calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Salario: '))
if salario > 1737.50:
    reajuste = salario + (salario/100)*10
    print('Salario anterior: R$ {}, salario com reajuste: R$ {}'.format(salario, reajuste))
else:
    reajuste = salario + (salario/100)*15
    print('Salario anterior: R$ {}, salario com reajuste: R$ {}'.format(salario, reajuste))
