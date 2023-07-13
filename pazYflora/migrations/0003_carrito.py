from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pazYflora', '0002_remove_producto_codid_producto_codigoid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(verbose_name='Precio Producto')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion de Envío')),
                ('datosPay', models.CharField(max_length=50, verbose_name='Datos Pay pal')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pazYflora.producto', verbose_name='Producto')),
            ],
        ),
    ]
