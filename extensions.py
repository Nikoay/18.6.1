import requests
import json
from Config import keys

class ConvertionExeption(Exception):
    pass

class Cryptoconverter:
    @staticmethod
    def get_prise(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')
        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base * amount