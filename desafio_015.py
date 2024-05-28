# Escreva um proghrama que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0.15 por km rodado

dias = int(input('diarias: '))
km = int(input('Km rodados: '))
print('valor de {} diarias: R$ {}\nValor de {} km rodados: R$ {}\nValor total: R$ {}'.format(dias, dias*60, km, km*0.15, (dias*60)+(km*0.15)))