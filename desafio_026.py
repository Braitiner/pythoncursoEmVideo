# Faça um programa que leia uma frase pelo teclado e mostre:
    # Quatas vezes apareceu a letra "A".
    # Em que posição ela aparece a primeira vez
    # Em que posição ela aparece a ultima vez

frase = input('Frase: ').upper().strip()
print(frase.count('A'))
print(frase.find("A"))
print(frase.rfind("A"))