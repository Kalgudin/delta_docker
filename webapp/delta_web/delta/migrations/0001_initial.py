# Generated by Django 4.1.3 on 2023-01-16 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100, verbose_name='название')),
                ('url', models.CharField(default='', max_length=1000, verbose_name='url')),
                ('shard', models.CharField(default='', max_length=100, verbose_name='shard')),
                ('query', models.CharField(default='', max_length=800, verbose_name='query')),
                ('updated_at', models.IntegerField(blank=True, null=True)),
                ('total_views', models.IntegerField(default=0)),
                ('parent_cat', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delta.category')),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Constants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.IntegerField(default=15, verbose_name='размер минимальной скидки отображаемого товара на странице')),
                ('paginate', models.IntegerField(default=20, verbose_name='количество товара на одной странице')),
                ('pages', models.IntegerField(default=50, verbose_name='количество страниц поиска товаров на Wildberries')),
                ('cache_time', models.IntegerField(default=60, verbose_name='время кэширования в секундах')),
            ],
            options={
                'verbose_name_plural': 'Константы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ИД продукта')),
                ('name', models.CharField(db_index=True, default='', max_length=100, verbose_name='Наименование')),
                ('base_price', models.IntegerField(default=0, verbose_name='базовая цена')),
                ('sale_price', models.IntegerField(db_index=True, default=0, verbose_name='цена со скидкой')),
                ('average_price', models.IntegerField(default=0, verbose_name='Средняя цена')),
                ('sale', models.IntegerField(db_index=True, default=0, verbose_name='Скидка от средней цены')),
                ('all_prices', models.JSONField(default=dict, verbose_name='Список цен')),
                ('feedbacks', models.IntegerField(default=0, verbose_name='колличество отзывов')),
                ('rating', models.IntegerField(default=0, verbose_name='рейтинг')),
                ('url', models.CharField(blank=True, max_length=300, verbose_name='url')),
                ('category', models.ManyToManyField(blank=True, to='delta.category', verbose_name='список категорий')),
            ],
            options={
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
