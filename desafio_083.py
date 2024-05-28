# Crie um programa onde o usuario digite uma expressao qualquer que use parenteses. seu aplicativo devera analisar se a expressão passada esta com os parenteses abertos e fechados na cordem correta.

expressao = str(input('Expressão: '))
lista = []
for i in expressao:
    lista.append(i)
if lista.count('(') > 0 and lista.count(')') > 0 and lista.count('(') == lista.count(')'):
    print('Expressao correta')
elif lista.count('(') == 0 and lista.count(')') == 0:
    print('Expressao correta')
else:
    print('expressao incorreta')
