class Menu:
    def __init__(self):
        self.divMenu = '=' * 40
        self.infoBot = 'CriptoBot / Versao: 1.1.1'
        self.desenvolvedor = 'Guilherme Malaquias'
        self.escolha = 1

    def inicial_menu(self) -> str:
        return f'{self.divMenu}\n1 - Consultar Moeda\n2 - Consultar Moeda Por Intervalo\n0 - Para sair\n{self.divMenu}'

    def mostra_moedas_menu(self) -> str:
        return f'{self.divMenu}\n1 - BTC-BRL (Bitcoin)\n2 - LTC-BRL (Litecoin)\n3 - ETH-BRL (Ethereum)\n4 - XRP-BRL (' \
               f'Ripple)\n{self.divMenu}'

    def escolha_menu(self, option: int):
        self.option = option
        self.temp = ''
        escolha_dic = {
            1: lambda temp: self.mostra_moedas_menu(),
            2: lambda temp: '\033[1;31mOpcao Indisponivel\033[m',
        }
        return escolha_dic[self.option](self.temp)


if __name__ == "__main__":
    c = Menu()
    print(c.escolha_menu(2))
