# Generated by Django 4.0.6 on 2022-12-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonificaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perseo',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
