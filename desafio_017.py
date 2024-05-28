# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
h = math.pow(co, 2) + math.pow(ca, 2)
h = math.sqrt(h)
print(h)