# Generated by Django 4.1 on 2022-10-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_store_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='japones',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
