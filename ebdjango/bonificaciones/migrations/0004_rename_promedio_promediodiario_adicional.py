# Generated by Django 4.0.6 on 2022-12-14 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonificaciones', '0003_alter_fenix_valor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promediodiario',
            old_name='promedio',
            new_name='adicional',
        ),
    ]
