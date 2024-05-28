# Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.

frase = str(input('Informe a frase: ')).replace(' ', "")
tamanho = len(frase)
frase_inversa = frase[::-1]
if frase == frase_inversa:
    print('É Polindromo')
else:
    print('Não é Polindromo')
