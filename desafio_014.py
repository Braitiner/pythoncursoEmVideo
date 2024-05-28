# Escreva um rpograma que converta uma temperatura digitada em ºC e converta para ºF.

valor = float(input('informe a temperatura em ºC: '))
print('A temperatura de {} ºC é {} ºF'.format(valor, (valor*9/5)+32))