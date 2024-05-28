# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
# Média abaixo de 5.0: Reprovado
# Média entre de 5.0 e 6.9 recuperacao
# Média 7.0 ou superior: Aprovado

from random import randint

n1 = randint(0,10)
n2 = randint(0,10)

media = (n1 + n2)/2

if media < 5:
    print('REPROVADO. Sua nota média foi de {:.2f}'.format(media))
elif media >= 5 and media < 7:
    print('RECUPERACAO. Sua nota média foi de {:.2f}'.format(media))
elif media >= 7:
    print('APROVADO. Sua nota média foi de {:.2f}'.format(media))