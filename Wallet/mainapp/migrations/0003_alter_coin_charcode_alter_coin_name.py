# Generated by Django 5.0.4 on 2024-04-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_coin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='charcode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='coin',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
