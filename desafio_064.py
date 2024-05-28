# Crie um programa quye leia vários números inteiros pelo teclado, O programa só vai parar quando o usuario digitar o valor 999, 
# que não é a condição de parada. No final mostre quantois números foram digitados e qual foi a soma entre eles 
# Desconsiderando o flog

stop = True
cont = 0
soma = 0
while stop:
    n = int(input('Digite um número: '))
    if n == 999:
        stop = False
    else:
        cont += 1
        soma += n
print('Foi digitado {} numeros e a soma deles são {}'.format(cont, soma))

