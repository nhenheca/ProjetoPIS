# Generated by Django 3.0.2 on 2020-01-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyracoes_main', '0007_ration_ration_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ration',
            name='ration_price',
            field=models.FloatField(verbose_name=0),
        ),
    ]