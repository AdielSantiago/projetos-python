from time import sleep

compras = list()
cont = 1

print( '=' * 30 )
print('{:^30}'.format('Listas de compras'))
print( '=' * 30 )

while True:
    compras.append(str(input(F'Qual o nome do {cont}º produto que  deseja adicionar a sua lista de compras?: ')))
    continuar = str(input('Deseja adicionar mais produtos?[sim/não]'))[0]
    cont += 1


    if continuar in 'Nn':
        print('-' * 51)
        break

print(F'Sua lista de compras está com os seguintes itens...\n{compras}\n')
print('-' * 30)
base = 999
while base != 4:
    print("""Para fazer alterações na lista considere as bases a seguir
    [1]-> Adicionar outros itens.
    [2]-> Remover itens.
    [3]-> Listar todos os itens.
    [4] -> encerrar programa.""")
    base = int(input('Qual a sua escolha?: '))
    print('-'* 30)

    if base == 1:
        while True:
            compras.append(str(input('Qual o novo iten que deseja adicionar?: ')))
            continuar = str(input('Quer continuar?[sim/não]: '))[0]
            print('-'*30)
            if continuar in 'Nn':
                print('-' * 30)
                break

    if base == 2:
        remover = str(input('Qual item você quer remover?: '))
        if remover not in compras:
            while remover not in compras:
                remover = str(input('Qual item você quer remover?: '))
        compras.remove(remover)
        print('-' * 30)

    if base == 3:
        print(F'Sua lista está da seguinte forma...\n{compras}')
        print('-' * 30)

    if base == 4:
        print('Algoritmo encerrado.')
        sleep(7)