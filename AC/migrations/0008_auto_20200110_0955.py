# Generated by Django 3.0.2 on 2020-01-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0007_polizas'),
    ]

    operations = [
        migrations.AddField(
            model_name='polizas',
            name='fin_poliza',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='polizas',
            name='inicio_poliza',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='polizas',
            name='nombre',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
