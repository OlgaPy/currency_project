# Generated by Django 4.2.4 on 2023-08-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RateSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency_app.currency')),
                ('rate_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency_app.ratesource')),
            ],
        ),
    ]
