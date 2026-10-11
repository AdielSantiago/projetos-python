numeros = list()
impares = list()
pares = list()

while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Deseja continuar?[Sim/não]: '))[0]
    print('=' * 20)
    if continuar in 'Nn':
        break

print(F'Na lista {numeros}...')

impares.sort()
pares.sort()

if len(impares) == 0:
    print('Não há números impares na lista.')
else:
    print(F'Os números ímpares são {impares}')

if len(pares) == 0:
    print('Não há números pares na lista')
else:
    print(F'Os números pares são {pares}')