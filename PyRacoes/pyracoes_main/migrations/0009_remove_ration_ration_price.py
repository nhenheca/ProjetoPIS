# Generated by Django 3.0.2 on 2020-01-02 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyracoes_main', '0008_auto_20200102_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ration',
            name='ration_price',
        ),
    ]