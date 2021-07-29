class Menu:

    def __init__(self):
        self.divMenu = '=' * 40
        self.infoBot = 'CriptoBot / Versao: 1.1.2'
        self.desenvolvedor = 'Guilherme Malaquias'

    def inicial_menu(self) -> str:
        return f'{self.divMenu}\n0 - Consultar Moeda\n1 - Consultar Moeda Por Intervalo\n\n2 - Para sair\n{self.divMenu}'

    def mostra_moedas_menu(self) -> str:
        return f'{self.divMenu}\n1 - BTC-BRL (Bitcoin)\n2 - LTC-BRL (Litecoin)\n3 - ETH-BRL (Ethereum)\n4 - XRP-BRL (' \
               f'Ripple)\n\n9 - Voltar\n{self.divMenu}'

    def decisao_menu(self) -> str:
        return f'Deseja continuar?\n1 - Sim\n2 - Nao\n{self.divMenu}'
