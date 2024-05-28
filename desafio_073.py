# Crie uma tupla preechida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A Apenas os cinco primeiros colocados
# B Os 4 ultimos colocados
# C Uma lista com os times em ordem alfabetica
# D Em que posição na tabela está o time da Goiás

times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Coritiba', 'Cuiabá', 'Fortaleza', 'Goiás', 'Grêmio', 'São Paulo', 'Santos', 'Vasco')

print(f'top 5 {times[0:5]}')
print(f'Zona de rebaixamento {times[-4:]}')
print(sorted(times))
print(f'Goiás esta na {times.index("Goiás")}ª posição')
