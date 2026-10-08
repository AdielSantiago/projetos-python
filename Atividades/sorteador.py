import os
from random import randint
from time import sleep

def limpa_tela():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def titulo():
    print('*' * 54)
    print(f'{'Sorteador de nomes':^54}')
    print('*' * 54)
    sleep(0.4)

def menu():
    interface = ['Sortear nome', 'Sair']
    print()
    print(f'{'-' * 24} Menu {'-' * 24}')

    cont = 1
    for i in interface:
        print(F'[{cont}]{'->':>2} {i:>4}')

        if cont == 1:
            print()
        cont += 1

    print('-' * 54)


nomes = []
titulo()

saldo = 1
while True:
    x = str(input(F'\nDigite o {saldo}º nome para o sorteio(precione apenas enter para parar): '))
    saldo += 1

    if x == '':
        break
    nomes.append(x)

limpa_tela()

while True:
    titulo()
    menu()

    try:
        base = int(input())
    except ValueError:
        print('ocorreu um erro na leitura das opções:(')
    else:
        if base == 1:
            quant = len(nomes)
            if quant == 0:
                break

            print('Sorteando...')
            sleep(1)

            nome_sort = randint(0, quant - 1)

            try:
                print(F'O nome sorteado foi {nomes[nome_sort]}')
                sleep(3.5)
                nomes.remove(nomes[nome_sort])
                limpa_tela()
            except IndexError:
                print('Não foi possível definir um vencedor:(')
            #print(nomes)

        elif base == 2:
            break

print('Saindo',end='')
for c in range(5):
    print('.',end='',flush=True)
    sleep(0.5)
sleep(0.3)