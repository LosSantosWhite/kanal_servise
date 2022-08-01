from django.db import models


class Order(models.Model):
    number = models.IntegerField("Номер заказа")
    usd_cost = models.DecimalField(
        "Стоимость в долл.США", max_digits=7, decimal_places=2
    )
    rub_cost = models.DecimalField("Стоимость в руб.", max_digits=7, decimal_places=2)
    shipment_date = models.DateField("Дата отгрузки")

    def __str__(self):
        return f"Заказ №{self.number} отгрузка {self.shipment_date}"

    class Meta:
        db_table = "orders"
