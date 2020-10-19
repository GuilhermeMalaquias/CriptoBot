from req import Request
from menu import Menu


requisicao = Request()
menu = Menu()


class Moedas:

    def escolha_menu(self, option: int):
        self.option = option
        escolha_dic = {
            1: lambda temp: self.escolhas_moeda(self.tmp_moeda),
            2: lambda temp: self.escolhas_moeda_intervalo(self.tmp_moeda),
        }
        if self.option not in escolha_dic.keys():
            raise KeyError
        print(menu.mostra_moedas_menu())
        self.tmp_moeda = int(input('Escolha:'))
        return escolha_dic[self.option](self.tmp_moeda)

    def escolhas_moeda(self, entrada_tipo_moeda: int):
        self.moeda = entrada_tipo_moeda
        self.tmp_moeda = ''
        self.moeda_dic = {
            1: lambda temp: requisicao.req('BTC'),
            2: lambda temp: requisicao.req('LTC'),
            3: lambda temp: requisicao.req('ETH'),
            4: lambda temp: requisicao.req('XRP'),
        }
        return self.moeda_dic[self.moeda](self.tmp_moeda)

    def escolhas_moeda_intervalo(self, entrada_tipo_moeda: int):
        self.moeda = entrada_tipo_moeda
        self.moeda_dic = {
            1: lambda temp: requisicao.req_intervalo_dia('BTC', self.tmp_moeda_intervalo),
            2: lambda temp: requisicao.req_intervalo_dia('LTC', self.tmp_moeda_intervalo),
            3: lambda temp: requisicao.req_intervalo_dia('ETH', self.tmp_moeda_intervalo),
            4: lambda temp: requisicao.req_intervalo_dia('XRP', self.tmp_moeda_intervalo),
        }
        if self.tmp_moeda not in self.moeda_dic.keys():
            raise KeyError
        self.tmp_moeda_intervalo = int(input("Informe o intervalo de Dias:"))
        if self.tmp_moeda_intervalo <= 0:
            raise ValueError
        return self.moeda_dic[self.moeda](self.tmp_moeda)


if __name__ == "__main__":
    moedas = Moedas()
    print(moedas.escolha_menu(2))
