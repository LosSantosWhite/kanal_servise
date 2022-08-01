from datetime import datetime
from decimal import Decimal
from pprint import pprint
from typing import Callable
import googleapiclient
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from orders.cbr.exchange_rates import get_rub_exchange

from django.conf import settings


class TableValues:
    SPREADSHEET_RANGE = settings.SPREADSHEET_RANGE

    def __init__(self, spreadsheet_id: str, credential_file) -> None:
        self.spreadsheet_id = spreadsheet_id
        self.credential_file = credential_file
        self.service = self.get_service(self.credential_file)

    @classmethod
    def get_service(cls, credential_file) -> googleapiclient.http.HttpRequest:
        # Возвращает объект для формирования запросов к GoogleAPI

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credential_file, settings.SPREADSHEET_SCOPES
        )
        httpAuth = credentials.authorize(httplib2.Http())
        return apiclient.discovery.build("sheets", "v4", http=httpAuth)

    def get_raw_values(self, major_dimension="ROWS"):
        # Получает сырые значения из таблицы
        return self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=self.SPREADSHEET_RANGE,
            majorDimension=major_dimension,
        ).execute()

    @staticmethod
    def count_exchange(rub_exchange: float) -> Callable:
        def insert_value(google_sheet_row: list):
            if len(google_sheet_row) != 4:
                return
            nonlocal rub_exchange
            # Стоимость в рублях
            rub_value = Decimal(google_sheet_row[2]) * Decimal(rub_exchange)
            # Строка к формату datetime
            date = google_sheet_row[-1]
            google_sheet_row[-1] = datetime.strptime(date.replace('.', '/'), "%d/%m/%Y")
            google_sheet_row.insert(3, rub_value)
            return google_sheet_row

        return insert_value

    def get_values(self, rub_exchange: float) -> list:
        values = self.get_raw_values()["values"]
        insert_value = self.count_exchange(rub_exchange)
        values = list(map(insert_value, values))
        return values


rub_exchange = get_rub_exchange()
google_sheet_values = TableValues(settings.SPREADSHEET_ID, settings.CREDENTIALS_FILE).get_values(rub_exchange)
