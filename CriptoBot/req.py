import requests
import json

class Request:
    def req(self, moeda):
        '''
        moeda = BTC-BRL
        moeda = LTC-BRL
        '''
        self.moeda = moeda
        self.request = requests.get(f'https://economia.awesomeapi.com.br/json/all/{self.moeda}')
        self.context = json.loads(self.request.text)
    def filterReq(self):
        self.name = self.context[self.moeda]['name']
        self.maxima = float(self.context[self.moeda]['high'])
        self.minima = float(self.context[self.moeda]['low'])
        return f'Nome da Moeda: {self.name}\nValor Maximo: R$ {self.maxima:.2f}\nValor Minimo: R$ {self.minima:.2f}'.replace('.', ',')
        
if __name__ == "__main__":
    c = Request()
    c.req('BTC')
    print(c.filterReq())

    