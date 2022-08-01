from celery import shared_task
from celery.utils.log import get_task_logger
from orders.cbr.exchange_rates import get_rub_exchange
from orders.google_api.get_table_values import google_sheet_values
from orders.controllers.controller import update_model
from orders.models import Order

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    rub_exchange = get_rub_exchange()
    logger.info(f"USD/RUB = {rub_exchange}")
    values_from_google_sheet = google_sheet_values
    update_model(values_from_google_sheet)
    logger.info('Model updated')



