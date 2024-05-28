# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# acima de 40: obesidade morbida

peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / altura**2

if imc < 18.5:
    print('seu IMC é {:.2f}, você está Abaixo do peso,'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('seu IMC é {:.2f}, você está com peso Ideal,'.format(imc))
elif imc >= 25 and imc < 30:
    print('seu IMC é {:.2f}, você está com sobrepeso,'.format(imc))
elif imc >= 30 and imc < 40:
    print('seu IMC é {:.2f}, você está com obesidade,'.format(imc))
elif imc > 40:
    print('seu IMC é {:.2f}, você está com obesidade morbida,'.format(imc))