# Generated by Django 3.0.2 on 2020-01-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyracoes_main', '0011_auto_20200112_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_animals',
            field=models.ManyToManyField(blank=True, null=True, to='pyracoes_main.Animal'),
        ),
    ]
