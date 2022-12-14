# Generated by Django 4.1 on 2022-11-05 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_store_district_alter_store_brandname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='cellPhone',
            field=models.CharField(max_length=50, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='store',
            name='ie',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='IE'),
        ),
        migrations.AlterField(
            model_name='store',
            name='observation',
            field=models.TextField(null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='store',
            name='primaryColor',
            field=models.CharField(max_length=50, verbose_name='Cor Primária'),
        ),
        migrations.AlterField(
            model_name='store',
            name='secondaryColor',
            field=models.CharField(max_length=50, verbose_name='Cor Secundária'),
        ),
        migrations.AlterField(
            model_name='store',
            name='terms',
            field=models.TextField(null=True, verbose_name='Termos'),
        ),
    ]
