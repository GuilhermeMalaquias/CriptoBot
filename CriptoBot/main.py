from menu import Menu
from moedas import Moedas
from req import Request
from time import sleep

menu = Menu()
tipo_moeda = Moedas()
requisicao = Request()


SAIR = 0

while True:
    print(menu.inicial_menu())
    escolha = int(input('Escolha:'))
    if escolha == SAIR:
        print('\033[1;33mSaindo...\033[m')
        sleep(2)
        print(f'Desenvolvedor: {menu.desenvolvedor}\n{menu.infoBot}')
        break
    try:
        tipo_moeda.escolha_menu(escolha)
        sleep(2)
    except KeyError:
        print('\033[1;31mOpcao Invalida\033[m')
    except ValueError:
        print('\033[1;31mInsira um valor Valido\033[m')
