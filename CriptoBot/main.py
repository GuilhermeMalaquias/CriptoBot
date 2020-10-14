from menu import Menu
from moedas import Moedas
from req import Request
from time import sleep

menu = Menu()
tipo_moeda = Moedas()
requisicao = Request()

sair = 0
while True:
    print(menu.inicial_menu())
    escolha_opcao = int(input('Escolha:'))
    if escolha_opcao == sair:
        print('Saindo...')
        sleep(2)
        print(f'Desenvolvedor: {menu.desenvolvedor}\n{menu.infoBot}')
        break
    elif escolha_opcao > 2 or escolha_opcao < 0:
        print('\033[1;31mOpcao Invalida\033[m')
    elif escolha_opcao == 1:
        print(menu.mostra_moedas_menu())
        escolha_moeda = int(input('Escolha:'))
        requisicao.req(tipo_moeda.escolhas_moeda(escolha_moeda))
        print(requisicao.filter_req())
        break
    elif escolha_opcao == 2:
        print('\033[1;31mOpcao Indisponivel\033[m')
