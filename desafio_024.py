# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input('Cidade: ').upper().split()
if 'SANTO' in cidade[0]:
    print('Cidade tem Santo no primeiro nome')
else:
    print('Cidade não tem Santo no primeiro nome')
    