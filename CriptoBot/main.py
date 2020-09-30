from menu import Menu
from moedas import Moedas
from req import Request

menu = Menu()
tipoMoedas = Moedas()
requisicao = Request()


menu.menuInicial()
tipoMoedas.moedas()

moeda = int(input('Informe a Moeda Desejada: '))
if moeda == 1:
    print(menu.divisorMenu)
    requisicao.req('BTC')
    print(requisicao.filterReq())
    print(menu.divisorMenu)
    
elif moeda == 2:
    print(menu.divisorMenu)
    requisicao.req('LTC')
    print(requisicao.filterReq())
    print(menu.divisorMenu)