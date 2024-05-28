# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a comdição de parada. 
# No final mostre quantos números foram digitados e qual foi a soma entre eles.

s = c = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Soma: {s}\nNumeros: {c}')
