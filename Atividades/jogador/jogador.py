jogadores = list()
jogador = dict()
lista_gols = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador?: '))
    n_partidas = int(input(F'Quantas paratidas {jogador['nome']} jogou?: '))
    lista_gols.clear()


    for c in range(n_partidas):
        lista_gols.append(int(input(F'Quantos gols o jogador marcou na {c + 1}º partida?: ')))

    jogador['gols'] = lista_gols[:]
    jogador['total_gols'] = sum(lista_gols)
    jogadores.append(jogador. copy())

    while True:
        resposta = str(input('Deseja continunar?[SIM/NÃO]: ')).upper()[0]

        if resposta in 'SN':
            break
        print('Erro. por favor digite "sim" ou "não" ')

    if resposta == 'N':
        break
print('-=' * 32)

print('=== DADOS DOs JOGADORES ===')

print('cod', end='')
for i in jogador.keys():
    print(F'{i:<13}', end='')
print()

print('-' * 36)

for k, v in enumerate(jogadores):
    print(F'{k:>1}- ',end='')

    for d in v.values():
        print(F'{str(d):<13}', end='')

    print()

print('-' * 36)

while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar): '))

    if busca == 999:
        break

    if busca >= len(jogadores):
        print(F'Erro! Não existe jogador com código {busca}!')
    else:
        print(F'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]['nome']}:')

        for i, g in enumerate(jogadores[busca]['gols']):
            print(F'   No jogo {i + 1} fez {g} gols.')

    print('-' * 40)