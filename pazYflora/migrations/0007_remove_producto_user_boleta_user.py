# Generated by Django 4.2.1 on 2023-07-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazYflora', '0006_producto_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='user',
        ),
        migrations.AddField(
            model_name='boleta',
            name='user',
            field=models.CharField(blank=True, max_length=100, verbose_name='Usuario'),
        ),
    ]