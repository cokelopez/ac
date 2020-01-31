# Generated by Django 3.0.2 on 2020-01-17 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0023_semanas'),
    ]

    operations = [
        migrations.CreateModel(
            name='pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('renta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AC.renta')),
                ('semana', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AC.semanas')),
            ],
        ),
    ]
