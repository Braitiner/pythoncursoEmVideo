# Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
for i in range(0,10):
    print(termo)
    termo += razao