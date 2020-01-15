# Generated by Django 3.0 on 2020-01-15 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=255)),
                ('animal_weight', models.FloatField()),
                ('animal_age', models.ManyToManyField(to='pyracoes_main.Age')),
            ],
        ),
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributes_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_animals', models.ManyToManyField(blank=True, to='pyracoes_main.Animal')),
                ('user_django', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ration_name', models.CharField(max_length=255)),
                ('ration_desc', models.TextField()),
                ('ration_image', models.CharField(max_length=2083)),
                ('ration_price', models.FloatField()),
                ('ration_age', models.ManyToManyField(to='pyracoes_main.Age')),
                ('ration_atrib', models.ManyToManyField(to='pyracoes_main.Attributes')),
                ('ration_classification', models.ManyToManyField(to='pyracoes_main.Classification')),
                ('ration_port', models.ManyToManyField(to='pyracoes_main.Port')),
                ('ration_type', models.ManyToManyField(to='pyracoes_main.Type')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_port',
            field=models.ManyToManyField(to='pyracoes_main.Port'),
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_type',
            field=models.ManyToManyField(to='pyracoes_main.Type'),
        ),
    ]
