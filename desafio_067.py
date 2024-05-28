# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usúario. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Tabuada de qual numero: '))
    if n < 1:
        break
    for i in range(1,11):
        print(f'{i} x {n} = {i*n}')
print('Fim')