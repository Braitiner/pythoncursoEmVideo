# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão

num = int(input('Informe um número: '))
index = int(input('Escolha uma opção para conversão:\n1 - Binário\n2 - Octal\n3 - hexadecimal\n>>>    '))

if index == 1:
    bin = bin(num)
    print('O numero {} convertido para binario é {}'.format(num, bin[2:]))

elif index == 2:
    octal = oct(num)
    print('O numero {} convertido para octal é {}'.format(num, octal[2:]))

elif index == 3:
    hexa = hex(num)
    print('O numero {} convertido para hexadecimal é {}'.format(num, hexa[2:]))
