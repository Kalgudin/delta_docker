from celery import shared_task

from datetime import datetime
from .models import Category, Visitors
from .proucts_def import get_product_for_db


@shared_task
def task_get_product_for_db(shard, query, cat):
    # print(f'Update Category {cat}---------------------')
    get_product_for_db(shard, query, cat)


@shared_task
def regular_update_products():
    category = Category
    for cat in category.objects.all():
        pora_obnovlyat = (datetime.now().timestamp() > (cat.updated_at + (60 * 60 * 24)))  # Раз в сутки
        if pora_obnovlyat:
            get_product_for_db(shard=cat.shard, query=cat.query, cat=cat.id)
        else:
            print(f'..... Category {cat.name} still fresh!!!!!')


@shared_task
def task_visit_counter(ip):
    vis, created = Visitors.objects.get_or_create(ip=ip)
    vis.count += 1
    vis.last_visit = datetime.now().timestamp()
    vis.save()
    # print('Visitor - ' + str(vis.ip))



