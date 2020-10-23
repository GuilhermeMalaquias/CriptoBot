class Menu:

    def __init__(self):
        self.divMenu = '=' * 40
        self.infoBot = 'CriptoBot / Versao: 1.1.1'
        self.desenvolvedor = 'Guilherme Malaquias'

    def inicial_menu(self) -> str:
        return f'{self.divMenu}\n1 - Consultar Moeda\n2 - Consultar Moeda Por Intervalo\n0 - Para sair\n{self.divMenu}'

    def mostra_moedas_menu(self) -> str:
        return f'{self.divMenu}\n1 - BTC-BRL (Bitcoin)\n2 - LTC-BRL (Litecoin)\n3 - ETH-BRL (Ethereum)\n4 - XRP-BRL (' \
               f'Ripple)\n{self.divMenu}'


