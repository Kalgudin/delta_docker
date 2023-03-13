from celery import shared_task

from datetime import datetime
from .models import Category
from .proucts_def import get_product_for_db


@shared_task
def update_goods():
    print('I am in TASKS - update_goods !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return True


@shared_task
def test_task(*args):
    print('!!!!!!!!!!!!!!!!!!!test_tusk!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(args, '****************************************')
    return True


@shared_task
def task_get_product_for_db(shard, query, cat):
    get_product_for_db(shard, query, cat)


@shared_task
def regular_update_products(*args):
    category = Category
    for cat in category.objects.all():
        pora_obnovlyat = (datetime.now().timestamp() > (cat.updated_at + (60 * 60 * 24)))  # Раз в сутки
        if pora_obnovlyat:
            task_get_product_for_db.delay(shard=cat.shard, query=cat.query, cat=cat.id)
        else:
            print(f',,..... Category {cat.name} still fresh!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(args)



