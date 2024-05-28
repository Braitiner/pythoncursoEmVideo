# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se entram no intervalo de 1 até 500.
s = 0
for i in range(1, 501):
    if (i%3) == 0 and (i%2) != 0:
        print(i)
        s += i
print('A soma dos numeros impares multiplo de 3 é {}'.format(s))