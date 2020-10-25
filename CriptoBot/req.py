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
        if self.request.status_code == 404:
            raise ConnectionError('Api indisponivel no momento')
        self.context = json.loads(self.request.text)
        return self.filter_req()

    def req_intervalo_dia(self, moeda: str, dias: int):
        self.moeda = moeda
        self.dias = dias
        self.request_intervalo = requests.get(f'{BASE_URL}daily/{self.moeda}/{self.dias}')
        self.context_intervalo = json.loads(self.request_intervalo.text)
        return self.filter_req_intervalo()

    def filter_req(self):
        self.name = self.context[self.moeda]['name']
        self.atual = float(self.context[self.moeda]['bid'])
        self.data = self.context[self.moeda]['timestamp']
        self.data = datetime.fromtimestamp(int(self.data)).strftime('%d/%m/%Y')
        print(f'{menu.divMenu}\nNome: {self.name}\nValor: R$ {self.atual:.2f}\nData: {self.data}\n{menu.divMenu}'.replace(
            '.',
            ','))

    def filter_req_intervalo(self):
        self.name = self.context_intervalo[0]['name']
        print(menu.divMenu)
        for item_name in range(len(self.context_intervalo)):
            print(f'Nome: {self.name}\n'
                  f'Valor: {float(self.context_intervalo[item_name]["bid"]):.2f}\n'
                  f'Data: {datetime.fromtimestamp(int(self.context_intervalo[item_name]["timestamp"])).strftime("%d/%m/%Y")}\n{menu.divMenu}'.replace(".", ","))
