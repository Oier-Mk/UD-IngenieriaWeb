# Generated by Django 3.2.8 on 2021-12-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mammamiaApp', '0003_alter_pizza_ingredientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='kcal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='kcal'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='origen',
            field=models.CharField(max_length=50, verbose_name='origin'),
        ),
        migrations.AlterField(
            model_name='masa',
            name='grosormm',
            field=models.IntegerField(verbose_name='width mm'),
        ),
        migrations.AlterField(
            model_name='masa',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='masa',
            name='supPrecio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='supplement'),
        ),
        migrations.AlterField(
            model_name='masa',
            name='tipoHarina',
            field=models.CharField(max_length=50, verbose_name='flour Type'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='price'),
        ),
    ]