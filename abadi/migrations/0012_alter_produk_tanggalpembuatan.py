# Generated by Django 4.1.2 on 2024-03-19 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abadi', '0011_rename_idsaldoawalbahanbaku_saldoawalartikel_idsaldoawalartikel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='TanggalPembuatan',
            field=models.DateField(),
        ),
    ]
