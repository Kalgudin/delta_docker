# Generated by Django 4.1.3 on 2023-01-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(db_index=True, default='', max_length=50, verbose_name='IP посетителя')),
                ('last_visit', models.IntegerField(blank=True, null=True, verbose_name='последнее посещение')),
                ('count', models.IntegerField(default=0, verbose_name='количество посещенй')),
            ],
            options={
                'verbose_name_plural': 'Посетители',
            },
        ),
    ]