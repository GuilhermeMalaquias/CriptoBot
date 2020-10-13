class Menu:
    def __init__(self):
        self.divisorMenu = '=' * 40
        self.infoBot = 'CriptoBot / Versao: 1.1.1'
        self.desenvolvedor = 'Guilherme Malaquias'

    def inicial_menu(self):
        return f'Seja Bem Vindo!\nDesenvolvedor: {self.desenvolvedor}\n{self.infoBot}'

    def escolha_menu(self) -> str:
        return '1 - Consultar Moeda\n2 - Consultar Moeda Por Intervalo\n0 - Para sair'


if __name__ == "__main__":
    c = Menu()
    print(c.inicial_menu())
    print(c.divisorMenu)
    print(c.escolha_menu())
