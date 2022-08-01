import django.db.models
from django.core.exceptions import ObjectDoesNotExist
from orders.models import Order


def update_model(values: list):
    Order.objects.all().delete()
    for value in values:
        try:
            order = Order.objects.get(number=value[1])
            order.number = value[1]
            order.usd_cost = value[2]
            order.rub_cost = value[3]
            order.shipment_date = value[4]
        except ObjectDoesNotExist:
            order = Order.objects.create(**{
                'number': value[1],
                'usd_cost': value[2],
                'rub_cost': value[3],
                'shipment_date': value[4]
            })

        order.save()
