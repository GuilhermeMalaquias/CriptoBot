from menu import Menu
from moedas import Moedas
from req import Request
from time import sleep

menu = Menu()
tipo_moeda = Moedas()
requisicao = Request()

while True:
    print(menu.inicial_menu())
    escolha = int(input('Escolha: '))
    if escolha == 0:
        print('\033[1;33mSaindo...\033[m')
        sleep(2)
        print(f'Desenvolvedor: {menu.desenvolvedor}\n{menu.infoBot}')
        break
    try:
        print(menu.escolha_menu(escolha))
        escolha_moeda = int(input('Escolha:'))
        requisicao.req(tipo_moeda.escolhas_moeda(escolha_moeda))
        print(requisicao.filter_req())
        break
    except KeyError:
        print('\033[1;31mOpcao Invalida\033[m')
