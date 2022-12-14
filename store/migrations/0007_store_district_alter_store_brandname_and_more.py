# Generated by Django 4.1 on 2022-11-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_store_email_remove_store_password_store_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='district',
            field=models.CharField(default='', max_length=255, verbose_name='Bairro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='brandName',
            field=models.CharField(max_length=255, verbose_name='Nome Fantasia'),
        ),
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='store',
            name='corporateName',
            field=models.CharField(max_length=255, verbose_name='Razão Social'),
        ),
        migrations.AlterField(
            model_name='store',
            name='document',
            field=models.CharField(max_length=100, unique=True, verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='store',
            name='ie',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='IE'),
        ),
        migrations.AlterField(
            model_name='store',
            name='number',
            field=models.CharField(max_length=50, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='store',
            name='paymentStatus',
            field=models.CharField(choices=[('1', 'Pago'), ('2', 'Pagamento Pendente')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='store',
            name='postalCode',
            field=models.CharField(max_length=50, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='store',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='store',
            name='street',
            field=models.CharField(max_length=255, verbose_name='Endereço'),
        ),
    ]
