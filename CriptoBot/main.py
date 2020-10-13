from menu import Menu
from moedas import Moedas
from req import Request
from time import sleep

menu = Menu()
tipo_moeda = Moedas()
requisicao = Request()

print(menu.divisorMenu)
print(menu.inicial_menu())

while True:
    print(menu.divisorMenu)
    print(menu.escolha_menu())
    escolha_opcao = int(input('Escolha:'))
    if escolha_opcao < 0 or escolha_opcao > 2:
        print(menu.divisorMenu)
        print('Opcao Invalida!')

    if escolha_opcao == 0:
        print('Saindo...')
        sleep(2)
        print('Programa finalizado!')
        break
    if escolha_opcao == 1:
        print(menu.divisorMenu)
        print(tipo_moeda.mostra_moedas())
        print(menu.divisorMenu)

        escolha_moeda = int(input('Escolha:'))

        print(menu.divisorMenu)
        requisicao.req(tipo_moeda.escolhas_moeda(escolha_moeda))
        print(requisicao.filter_req())

    elif escolha_opcao == 2:
        print(menu.divisorMenu)
        print('Indisponivel no momento!')
