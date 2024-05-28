# Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. 
# No final, mostre os valores pares e impares em ordem crescente.

lista = []
par = []
impar = []
for i in range(7):
    num = int(input('Numero: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
lista.append(sorted(par))
lista.append(sorted(impar))
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
