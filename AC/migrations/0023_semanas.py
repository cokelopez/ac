# Generated by Django 3.0.2 on 2020-01-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0022_renta'),
    ]

    operations = [
        migrations.CreateModel(
            name='semanas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diainicio', models.DateField()),
                ('diafin', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
