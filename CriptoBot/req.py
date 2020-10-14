from menu import Menu
from datetime import datetime
import json
import requests


menu = Menu()


BASE_URL = 'https://economia.awesomeapi.com.br/json/'


class Request:
    def req(self, moeda: str):
        """
        moeda = BTC-BRL
        moeda = LTC-BRL
        """
        self.moeda = moeda
        self.request = requests.get(f'{BASE_URL}all/{self.moeda}')
        self.context = json.loads(self.request.text)

    def req_intervalo_dia(self):
        self.request_intervalo = requests.get(f'{BASE_URL}daily/{self.moeda}/{self.dias}')
        self.context_intervalo = json.loads(self.request_intervalo.text)

        # for iten in self.context_intervalo:
        #   print(iten['bid'])

    def filter_req(self):
        self.name = self.context[self.moeda]['name']
        self.atual = float(self.context[self.moeda]['bid'])
        self.data = self.context[self.moeda]['timestamp']
        self.data = datetime.fromtimestamp(int(self.data)).strftime('%d/%m/%Y')

        return f'{menu.divMenu}\nNome: {self.name}\nValor: R$ {self.atual:.2f}\nData: {self.data}\n{menu.divMenu}'.replace('.', ',')


if __name__ == "__main__":
    c = Request()
    c.req('BTC')
    print(c.filter_req())
