# Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas
    # O nome com todas as letras minúsculas
    # Quantas letras ao todo (sem considerar espaços).
    # Quantas letras tem o primeiro nome.

nome = input('Nome completo: ')
print('Maiúscula ',nome.upper())
print('Minuscula ',nome.lower())
print(len(nome.replace(' ','')))
print(len( nome.split()[0]))