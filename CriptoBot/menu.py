class Menu:
    def __init__(self):
        self.divisorMenu = '='*40
        self.infoBot = 'BotBitcoin / Versao: 1.1.1'
        self.desenvolvedor = 'Guilherme Malaquias da Silva'
    def menuInicial(self):
        print('Seja Bem Vindo!')
        print(self.divisorMenu)
        print(f'Desenvolvido Por: \n{self.desenvolvedor}')
        print(f'\n{self.infoBot}')
        print(self.divisorMenu)

if __name__ == "__main__":
    c = Menu()
    c.menuInicial()