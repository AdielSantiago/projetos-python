from random import randint
from time import sleep

print('{:=^50}'.format(' Pedra Papel e Tesoura '))
opção = int(input("""Escolha sua jogada de acordo com as bases a seguir
[0] Pedra
[1] papel
[2] tesoura
Sua jogada: """))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

itens = ('pedra', 'papel', 'tesoura')
jogada_computador = randint(0, 2)

print('=-' * 8 )
print('Eu joguei:{}'.format(itens[jogada_computador]))
print('-' * 15)
print('Você jogou:{}'.format(itens[opção]))
print('=-' * 8)

if jogada_computador == 0:  # pc escolheu pedra
    if opção == 0:
        print('Empate')
    elif opção == 1:
        print('Você venceu')
    elif opção == 2:
        print('Você perdeu')
    else:
        print('Jogada inválida')

elif jogada_computador == 1: # pc escolheu papel
    if opção == 0:
        print('Você perdeu')
    elif opção == 1:
        print('Empate')
    elif opção == 2:
        print('Você Venceu')
    else:
        print('Jogada inválida')

elif jogada_computador == 2: # pc escolheu tesoura
    if opção == 0:
        print('Você Venceu')
    elif opção == 1:
        print('Você Perdeu')
    elif opção == 2:
        print('Empate')
    else:
        print('Jogada inválida')

sleep(30)