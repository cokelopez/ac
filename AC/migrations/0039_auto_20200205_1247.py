# Generated by Django 3.0.2 on 2020-02-05 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0038_auto_20200205_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagos',
            name='semana2',
        ),
        migrations.AlterField(
            model_name='carros',
            name='conductor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='AC.Conductores'),
        ),
        migrations.AlterField(
            model_name='carros',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AC.Propietarios'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AC.Carros'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='gasto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AC.TipoGasto'),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AC.Carros'),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='renta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AC.Renta'),
        ),
        migrations.AlterField(
            model_name='polizas',
            name='carro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AC.Carros'),
        ),
        migrations.AlterField(
            model_name='renta',
            name='carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AC.Carros'),
        ),
    ]
