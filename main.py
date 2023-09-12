from time import sleep
from random import choice
lista = ["PEDRA", "PAPEL", "TESOURA"]
escolhido = choice(lista)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input("Qual é a sua jogada? "))
if opcao >= 3:
    print("Opção invalida, tente novamente.")
else:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!!!")
    sleep(1)
    print(10 * "-=-")
    print("computador jogou {}".format(escolhido))
    if opcao == 0:
        print("Jogador escolheu PEDRA")
    elif opcao == 1:
        print("Jogador escolheu PAPEL")
    elif opcao == 2:
        print("Jogador escolheu TESOURA")
    print(10 * "-=-")
    if escolhido == lista[0]:
        if opcao == 0:
            print("EMPATE")
        elif opcao == 1:
            print("Jogador GANHOU!")
        elif opcao == 2:
            print("Computador GANHOU!")
    if escolhido == lista[1]:
        if opcao == 0:
            print("Computador GANHOU!")
        elif opcao == 1:
            print("EMPATE!")
        elif opcao == 2:
            print("Jogador GANHOU!")
    if escolhido == lista[2]:
        if opcao == 0:
            print("Jogador GANHOU!")
        elif opcao == 1:
            print("Computador GANHOU!")
        elif opcao == 2:
            print("EMPATE!")
