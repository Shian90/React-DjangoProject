# Generated by Django 4.0.4 on 2022-05-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculation', '0005_history_algotype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacci',
            name='output',
            field=models.TextField(),
        ),
    ]
