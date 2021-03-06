# Generated by Django 3.0.7 on 2020-07-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0009_auto_20200701_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalincome',
            name='amount_only',
            field=models.FloatField(null=True, verbose_name='Zapisywana kwota dodatkowa (*można pozostawić wolne)'),
        ),
        migrations.AlterField(
            model_name='additionalincome',
            name='amount_with_monthly',
            field=models.FloatField(null=True, verbose_name='Kwota dodatkowa wraz z miesięcznymi wpływami (*można pozostawić wolne)'),
        ),
        migrations.AlterField(
            model_name='additionalincome',
            name='income_description',
            field=models.CharField(max_length=128, null=True, verbose_name='Opis dla wpisywanego dodatkowego przychodu'),
        ),
    ]
