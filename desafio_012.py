# faça um algoritimo que leia a preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input("informe o proço do produto: "))
print('O valor do produto é R$ {:.2f} aplicando o desonto de 5 porcento fica R$ {:.2f}'.format(valor, valor-((valor/100)*5)))