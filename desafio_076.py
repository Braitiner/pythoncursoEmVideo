# Crie um programa que tenha uma tupla única com nomes de produtos e seu respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organiz\do os dados em forma tabular.

tupla = ('teclado', 89.9, 'Mouse', 49.90, 'Mousepad', 29.90, 'Headfone', 249.9, 'Monitor', 599.9, 'Webcam', 129.9, 'Caixa de Som', 199.9, 'Microfone', 99.9, 'Impressora', 299.9, 'Scanner', 199.9, 'Multifuncional', 399.9, 'Papel A4', 19.9, 'Pen Drive', 29.9, 'Cartão de Memória', 49.9, 'HD Externo', 149.9, 'SSD', 399.9, 'Cabo HDMI', 29.9, 'Cabo USB', 19.9, 'Cabo VGA', 19.9, 'Cabo de Força', 19.9, 'Teclado Gamer', 199.9, 'Mouse Gamer', 149.9, 'Headfone Gamer', 299.9, 'Cadeira Gamer', 999.9, 'Notebook', 2999.9, 'Desktop', 2499.9, 'Celular', 1999.9, 'Tablet', 1499.9, 'Console de Jogos', 2999.9, 'Jogo de Videogame', 199.9, 'Cartão de Jogo', 99.9, 'Fone de Ouvido', 199.9, 'Aparelho de Som', 299.9, 'Home Theater', 499.9, 'Smart TV', 1999.9, 'Televisão LED', 1499.9, 'Televisão LCD', 1299.9)

for i in range(0, len(tupla), 2):
    print(f'{tupla[i]:.<30} R$  {tupla[i+1]:6<.2f}')