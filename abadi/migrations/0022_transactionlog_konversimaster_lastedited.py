# Generated by Django 4.1.4 on 2024-04-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abadi', '0021_penyesuaian_konversi'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactionlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('waktu', models.DateTimeField()),
                ('jenis', models.CharField(max_length=50)),
                ('pesan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='konversimaster',
            name='lastedited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
