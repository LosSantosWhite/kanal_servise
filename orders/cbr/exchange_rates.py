from xml import etree

import requests
from lxml import etree
import datetime


def get_rub_exchange(currency_code: str = "USD") -> float:
    # Возвращает последний курс обмена "currency_code" по умолчанию код Валюты США
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={today}"
    response = requests.get(url).content
    tree = etree.fromstring(response)

    for _ in tree.iter('Valute'):
        if _[1].text == currency_code:
            value = _[-1].text.replace(',', '.')
    return float(value)