# Generated by Django 4.1 on 2022-10-29 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_store_japones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='japones',
        ),
    ]
