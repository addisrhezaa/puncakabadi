# Generated by Django 4.1.2 on 2024-03-20 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abadi', '0014_spk_nomorpo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spk',
            name='NomorPO',
        ),
    ]
