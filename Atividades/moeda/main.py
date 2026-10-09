from time import sleep
import fun_moedas

valor = fun_moedas.scanner('Digite um valor: R$')
taxa = float(input('Taxa: '))
fun_moedas.resumo(valor, taxa)