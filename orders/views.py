from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint
from orders.models import Order
from orders.cbr.exchange_rates import get_rub_exchange
from orders.google_api.get_table_values import google_sheet_values


def index(request):
    obj = Order.objects.all()
    return HttpResponse(obj)
