import requests
import json
from config import currency

class ConvertionException(Exception):
    pass

class CurrencyMethod:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException("Одинаковые валюты нельзя конвертировать.")

        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = currency[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}")

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/f07e180fd954517ac009b6a7/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)
        return total_base["conversion_rate"] * amount
