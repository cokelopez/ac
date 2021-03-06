# Generated by Django 3.0.2 on 2020-01-10 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0006_auto_20200109_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='polizas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('carro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AC.carros')),
            ],
        ),
    ]
