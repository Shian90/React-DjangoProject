# Generated by Django 4.0.4 on 2022-05-13 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Calculation', '0006_alter_fibonacci_output'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='algoId',
            new_name='aid',
        ),
    ]
