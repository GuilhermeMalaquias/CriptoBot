from req import Request
from menu import Menu


requisicao = Request()
menu = Menu()

INTERVALO_NAO_ZERO_OU_NEGATIVO = 0
VOLTAR = 9


class Moedas:
    def escolha_menu(self, option: int):
        self.option = option
        escolha_dic = {
            0: lambda temp: self.escolhas_moeda(self.tmp_moeda),
            1: lambda temp: self.escolhas_moeda_intervalo(self.tmp_moeda),
        }
        if self.option not in escolha_dic.keys():
            raise KeyError
        else:
            print(menu.mostra_moedas_menu())
            self.tmp_moeda = int(input('Escolha:'))
            if self.tmp_moeda == VOLTAR:
                return ''
            else:
                return escolha_dic[self.option](self.tmp_moeda)

    def escolhas_moeda(self, entrada_tipo_moeda: int):
        self.moeda = entrada_tipo_moeda
        self.tmp_moeda = ''
        self.moeda_dic = {
            1: lambda temp: requisicao.req('bitcoin'),
            2: lambda temp: requisicao.req('litecoin'),
            3: lambda temp: requisicao.req('ethereum'),
            4: lambda temp: requisicao.req('ripple'),
        }
        if self.moeda not in self.moeda_dic.keys():
            
            raise KeyError
        else:
            return self.moeda_dic[self.moeda](self.tmp_moeda)

    def escolhas_moeda_intervalo(self, entrada_tipo_moeda: int):
        self.moeda = entrada_tipo_moeda
        self.moeda_dic = {
            1: lambda temp: requisicao.req_intervalo_dia('bitcoin', self.tmp_moeda_intervalo),
            2: lambda temp: requisicao.req_intervalo_dia('litecoin', self.tmp_moeda_intervalo),
            3: lambda temp: requisicao.req_intervalo_dia('ethereum', self.tmp_moeda_intervalo),
            4: lambda temp: requisicao.req_intervalo_dia('ripple', self.tmp_moeda_intervalo),
        }
        if self.tmp_moeda not in self.moeda_dic.keys():
            print("Aqui")
            raise KeyError
        self.tmp_moeda_intervalo = int(input("Informe o intervalo de Dias:"))
        
        if self.tmp_moeda_intervalo <= INTERVALO_NAO_ZERO_OU_NEGATIVO:
            raise ValueError

        else:
            return self.moeda_dic[self.moeda](self.tmp_moeda)
