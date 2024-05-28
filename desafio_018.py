# Faça um programa que leia um Ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente dese Ângulo.
import math

ang = float(input('informe o angulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O Angulo {} tem o seno {:.4f} o cosseno {:.4f} e a tangente {:.4f}'.format(ang, seno, cos, tang))
