# Generated by Django 4.0.4 on 2022-05-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algos',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Factorial',
            fields=[
                ('algos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Calculation.algos')),
                ('value', models.IntegerField()),
                ('output', models.IntegerField()),
            ],
            bases=('Calculation.algos',),
        ),
        migrations.CreateModel(
            name='Fibonacci',
            fields=[
                ('algos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Calculation.algos')),
                ('value', models.IntegerField()),
                ('output', models.IntegerField()),
            ],
            bases=('Calculation.algos',),
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('algos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Calculation.algos')),
                ('value', models.IntegerField()),
                ('output', models.IntegerField()),
            ],
            bases=('Calculation.algos',),
        ),
        migrations.CreateModel(
            name='SquareRoot',
            fields=[
                ('algos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Calculation.algos')),
                ('value', models.IntegerField()),
                ('output', models.FloatField()),
            ],
            bases=('Calculation.algos',),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('hisId', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('algoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Calculation.algos')),
            ],
        ),
    ]
