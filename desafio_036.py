# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo sera negado

valor = float(input('Valor imovel: '))
salario = float(input('Salario: '))
anos = int(input('Quantos de financiamento: '))

prestacao = (valor/anos)/12
if prestacao > salario * 0.30:
    print('Emprestimo negado, a prestação de {:.2f} é maior que 30 porcento do seu salário que é {:.2f}'.format(prestacao, salario*0.30))
elif prestacao <= salario * 0.30:
    print('Emprestimo aprovado, a prestação é {:.2f},  menor que 30 porcento do seu salário que é {:.2f}'.format(prestacao, salario*0.30))