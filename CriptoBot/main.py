from menu import Menu
from moedas import Moedas
from req import Request
from time import sleep

menu = Menu()
tipo_moeda = Moedas()
requisicao = Request()


SAIR = 2


while True:
    print(menu.inicial_menu())
    escolha = int(input('Escolha:'))
    if escolha == SAIR:
        print('Saindo...')
        sleep(2)
        print(f'Desenvolvedor: {menu.desenvolvedor}\n{menu.infoBot}')
        break
    try:
        tipo_moeda.escolha_menu(escolha)
        sleep(2)
    except KeyError:
        print('Opcao Invalida')
    except ValueError:
        print('Insira um valor Valido')
