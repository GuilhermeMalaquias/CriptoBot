class Moedas:
    def moedas(self):
        self.moedas = {'BTC': 1, 'LTC': 2}
        print(f'Moedas: {self.moedas}')


if __name__ == "__main__":
    moedas = Moedas()
    moedas.moedas()