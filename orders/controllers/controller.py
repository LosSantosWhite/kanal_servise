import django.db.models

from orders.models import Order


def update_model(values: list, model: django.db.models.Model = Order):
    for value in values:
        try:
            order = model.objects.get(id=value[0])
        except model.DoesNotExist:
            order = model.objects.create(**{

            })
        order.update(**{
            'number': value[1],
            'usd_cost': value[2],
            'rub_cost': value[3],
            'shipment_date': value[4]
        })
