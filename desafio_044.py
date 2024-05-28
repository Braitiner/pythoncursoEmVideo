# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
#a vista dinhheiro: -10%
# a vista cartao: -5%
# 2 x credito: sem juros
# 3x ou mais: + 20%

preco = float(input('Preço: '))
forma = int(input('Forma de pagamento:\n1 - Dinheiro\n2 - A vista cartao de debito ou credito\n3 - Parcelado\n >>>  '))

if forma == 1:
    print('Pagando no dinheiro tem desconto de R$ {:.2f}, o valor é de R$ {:.2f}'.format(preco*0.1,preco*0.9))
elif forma == 2:
    print('Pagando no cartao a vista tem desconto de R$ {:.2f}, o valor é de R$ {:.2f}'.format(preco*0.05,preco*0.95))
elif forma == 3:
    parcelas = int(input('Quantas parcelas: '))
    if parcelas == 2:
        print('Pagando no parcelao em {}x sem juros, o valor de cada parcela é de R$ {:.2f} valor total é R$ {:.2f}'.format(parcelas, preco/parcelas,preco))
    elif parcelas > 2:
        print('Pagando parcelado em {}x com acrescimo de 20% no total do produto, o valor de cada parcela é de R$ {:.2f} valor total é R$ {:.2f}'.format(parcelas, (preco*1.2)/parcelas,preco*1.2))
