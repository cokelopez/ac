# Generated by Django 3.0.2 on 2020-01-13 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0020_auto_20200113_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gasto',
            options={'ordering': ['fecha'], 'verbose_name_plural': 'Gastos'},
        ),
    ]
