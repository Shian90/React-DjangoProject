# Generated by Django 4.0.4 on 2022-05-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculation', '0004_alter_history_algoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='algoType',
            field=models.CharField(default=None, max_length=20),
        ),
    ]