# Generated by Django 4.2.1 on 2023-07-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazYflora', '0005_detalleboleta_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='user',
            field=models.CharField(blank=True, max_length=100, verbose_name='Usuario'),
        ),
    ]
