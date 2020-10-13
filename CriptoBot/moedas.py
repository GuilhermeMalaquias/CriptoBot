class Moedas:
    def mostra_moedas(self):
        return '1 - BTC-BRL (Bitcoin)\n2 - LTC-BRL (Litecoin)\n3 - ETH-BRL (Ethereum)\n4 - XRP-BRL (Ripple)'

    def escolhas_moeda(self, entrada_tipo_moeda: int) -> str:
        self.moeda = entrada_tipo_moeda
        if self.moeda == 1:
            return 'BTC'
        elif self.moeda == 2:
            return 'LTC'
        elif self.moeda == 3:
            return 'ETH'
        elif self.moeda == 4:
            return 'XRP'


if __name__ == "__main__":
    moedas = Moedas()
    print(moedas.moedas())
    print(moedas.escolhas_moeda(1))
