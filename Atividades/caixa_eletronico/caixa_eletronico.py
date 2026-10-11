from time import sleep

print('=' * 30)
print('{:^30}'.format('BANCO'))
print('=' * 30)

saque = int(input('Qual valor deseja sacar? R$'))

valor = saque
ced = 50
totced = 0

while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            
        totced = 0  
        
        if valor == 0:
            break

print('=' * 30)
print('Volte sempre')

sleep(2)