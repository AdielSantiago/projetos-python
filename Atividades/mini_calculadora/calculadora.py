from time import sleep

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite mais um valor: '))

maior_valor = 0
option = 0

while option != 5:
    
    print("""Com esses númeors você deseja...
    [1] - somar 
    [2] - multiplicar
    [3] - ver o maior
    [4] - adicionar outros números
    [5] - Sai do programa""")
    option = int(input('Qual é a sua opção?' ))
    
    if option == 1:
        print('A soma entre {} + {} é {} '.format(n1, n2,  n1 + n2 ))
    elif option == 2:
        print('A expressão {} X {} resulta em  {}'.format(n1, n2,  n1 * n2 ))
    elif option == 3:
        if n1 == n2:
            print('Os dois valores são iguais')
        if n1 > n2:
            maior_valor = n1
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior_valor))
        if n2 > n1:
            maior_valor = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior_valor ))
    elif option == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite mais um valor: '))
    elif option == 5:
        print('Encerrando...')
    else:
        print('A opção que você escolheu não é válida. tente novamente')
    sleep(1.5)

print('_' * 20)
print('Algoritmo finalizado.')

sleep(1.5)