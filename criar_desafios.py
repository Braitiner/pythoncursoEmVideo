import os

# Diretório onde estão os arquivos dos desafios
diretorio_desafios = 'Desafios'

# Loop para criar arquivos de desafio_031.py até desafio_100.py
for numero_desafio in range(31, 101):
    nome_arquivo = f'desafio_{numero_desafio:03}.py'
    caminho_arquivo = os.path.join(diretorio_desafios, nome_arquivo)

    # Verifica se o arquivo já existe antes de criar
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w') as arquivo:
            # Escreve algo no arquivo, por exemplo, um comentário
            arquivo.write(f'# Código do Desafio {numero_desafio}')

    print(f'Criado o arquivo: {caminho_arquivo}')
