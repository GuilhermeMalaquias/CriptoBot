from menu import Menu
from datetime import datetime
import json
import requests

menu = Menu()

BASE_URL = 'https://api.coingecko.com/api/v3/'


class Request:
    def req(self, moeda: str):
        """
        moeda = BTC-BRL
        moeda = LTC-BRL
        """
        self.moeda = moeda
        self.request = requests.get(f'{BASE_URL}/coins/{self.moeda}')
        if self.request.status_code == 404:
            raise ConnectionError('Api indisponivel no momento')
        
        self.context = self.request.json()
        return self.filter_req()

    def req_intervalo_dia(self, moeda: str, dias: int):
        self.moeda = moeda
        self.dias = dias
        self.request_intervalo = requests.get(f'{BASE_URL}coins/{self.moeda}/market_chart?vs_currency=brl&days={self.dias}&interval=daily')
        self.context_intervalo = self.request_intervalo.json()
        return self.filter_req_intervalo()
        # coins/bitcoin/market_chart?vs_currency=usd&days=10&interval=daily

    def filter_req(self):
        self.name = self.context['name']
        self.atual = float(self.context['market_data']['current_price']['brl'])
        # self.data = self.context['market_data']['ath_date']['brl']
        # self.data = datetime.fromtimestamp(int(self.data)).strftime('%d/%m/%Y')
        print(f'{menu.divMenu}\nNome: {self.name}\nValor: R$ {self.atual:.2f}\n{menu.divMenu}'.replace(
            '.',
            ','))

    def filter_req_intervalo(self):
        print(menu.divMenu)
        for i in self.context_intervalo['prices']:
            
            print('Nome: {}\nData: {}\nValor: {}\n{}'.format(self.moeda.capitalize(), *i,menu.divMenu))
            


              

