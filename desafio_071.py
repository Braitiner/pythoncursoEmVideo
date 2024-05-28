# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o
# programa vai informar quantas cedulas de cada valor serão entregues.
#Obs: Considere que o caixa possui cédulas de R$200, R$100, R$50,00, R$20, R$10, R$5 e R$2


while True:
    saque = int(input("Valor do saque: "))
    if saque == 1 or saque % 10 == 1:
        print('Não temos cedulas de 1, favor informar novo valor para saque.')
    else:
        print(f'você vai receber ',end='')
        if (saque // 200) > 0:
            nota_duzentos = saque // 200
            saque -= nota_duzentos * 200
            print(f'{nota_duzentos} nota(s) de R$ 200\n')
        if (saque // 100) > 0:
            nota_cem = saque // 100
            saque -= nota_cem * 100
            print(f'{nota_cem} nota(s) de R$ 100\n')
        if (saque // 50) > 0:
            nota_cinquenta = saque // 50
            saque -= nota_cinquenta * 50
            print(f'{nota_cinquenta} nota(s) de R$ 50\n')
        if (saque // 20) > 0:
            nota_vinte = saque // 20
            saque -= nota_vinte * 20
            print(f'{nota_vinte} nota(s) de R$ 20\n')
        if (saque // 10) > 0:
            nota_dez = saque // 10
            saque -= nota_dez * 10
            print(f'{nota_dez} nota(s) de R$ 10\n')
        if (saque // 5) > 0:
            nota_cinco = saque // 5
            saque -= nota_cinco * 5
            print(f'{nota_cinco} nota(s) de R$ 5\n')
        if (saque // 2) > 0:
            nota_dois = saque // 2
            saque -= nota_dois * 2
            print(f'{nota_dois} nota(s) de R$ 2\n')
        break    


