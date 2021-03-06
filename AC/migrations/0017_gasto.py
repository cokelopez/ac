# Generated by Django 3.0.2 on 2020-01-10 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0016_tipogasto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('iva', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AC.carros')),
                ('gasto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AC.tipoGasto')),
            ],
        ),
    ]
