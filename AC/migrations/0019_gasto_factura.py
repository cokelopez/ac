# Generated by Django 3.0.2 on 2020-01-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0018_gasto_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='factura',
            field=models.FileField(blank=True, null=True, upload_to='facturas/'),
        ),
    ]
