# Crie um programa que leia dois valores e mostre um menu na tela:

#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso
reset = True

while reset:
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    menu = 0
    
    while menu < 1 or menu > 5:
        menu = int(input('Escolha:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa\n >>> '))
        
        if menu == 1:
            print('Soma:', n1 + n2)
        elif menu == 2:
            print('Multiplicação:', n1 * n2)
        elif menu == 3:
            print('Maior número:', max(n1, n2))
        elif menu == 4:
            reset = True
        elif menu == 5:
            reset = False
        else:
            print('Opção inválida! Por favor, escolha uma opção entre 1 e 5.')
