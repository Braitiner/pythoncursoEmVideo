# faça um progama que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
    # ex: Ana Maria de Souza
    # primeiro = Ana
    # último = Souza

nome = input('Nome completo: ').title().split()
print('primeiro= {}\núltimo = {}'.format(nome[0], nome[len(nome)-1]))
