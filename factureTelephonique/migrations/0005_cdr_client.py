# Generated by Django 3.0.7 on 2020-06-11 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factureTelephonique', '0004_remove_cdr_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdr',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='factureTelephonique.Client'),
        ),
    ]
