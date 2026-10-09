def dobro(p = 0, form = False):
    total_d = p * 2
    return total_d if not form else pradrao(total_d)

def metade(p = 0, form = False):
    total_m = p / 2
    return total_m if form == False else pradrao(total_m)

def aumentar(a = 0, b = 0, form = False):
    aumento = a * ( b/100 )
    total_a = a + aumento
    return total_a if form == False else pradrao(total_a)

def diminuir(a = 0, b = 0, form = False):
    regresso = a * ( b/100 )
    total_di = a - regresso
    return total_di if form == False else pradrao(total_di)

def pradrao(valor, monetario = 'R$'):
    return f'{monetario}{valor:.2f}'.replace('.', ',')

def resumo(valor = 0, taxa = 0):
    print('*' * 30 )
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30 )
    print(F'Preço analisado: \t{pradrao(valor)}')
    print(F'Dobro do valor: \t{dobro(valor, form=True)}\nMetade do valor: \t{metade(valor,form=True)}')
    print(F'Aumento de {taxa}%: \t{aumentar(valor, taxa, form=True)}\nRedução de {taxa}%: \t{diminuir(valor, taxa, form=True)}')
    print('_' * 30)

def scanner(msg):

    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')

        if entrada.isalpha():
            print(F'Erro. "{entrada}" não é um valor válido')
        else:
            valido = True
            return float(entrada)