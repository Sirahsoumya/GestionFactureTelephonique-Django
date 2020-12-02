# Generated by Django 3.0.7 on 2020-06-07 21:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomClient', models.CharField(max_length=200, verbose_name='Nom du client')),
                ('numClient', models.CharField(max_length=200, verbose_name='Télephone')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dureeTotal', models.TimeField(verbose_name='Durée total')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factureTelephonique.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Cdr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('dureeAppel', models.TimeField(verbose_name="durée de l'appel")),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factureTelephonique.Facture')),
            ],
        ),
    ]
