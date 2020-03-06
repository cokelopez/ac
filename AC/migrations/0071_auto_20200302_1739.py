# Generated by Django 3.0.2 on 2020-03-02 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AC', '0070_auto_20200302_1233'),
    ]

    operations = [
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
            model_name='inactividad',
            name='carro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AC.Carros'),
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
