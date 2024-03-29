# Generated by Django 4.1.2 on 2024-03-12 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abadi', '0002_remove_detailsppb_nospk_detailsppb_detailspk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailkonversiproduksi',
            name='KodePenyesuaian',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.penyesuaian'),
        ),
        migrations.AlterField(
            model_name='detailspk',
            name='KodeArtikel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.artikel'),
        ),
        migrations.AlterField(
            model_name='detailspk',
            name='NoSPK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.spk'),
        ),
        migrations.AlterField(
            model_name='detailsppb',
            name='DetailSPK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='abadi.detailspk'),
        ),
        migrations.AlterField(
            model_name='detailsppb',
            name='NoSPPB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.sppb'),
        ),
        migrations.AlterField(
            model_name='detailsuratjalanpembelian',
            name='KodeProduk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.produk'),
        ),
        migrations.AlterField(
            model_name='detailsuratjalanpembelian',
            name='NoSuratJalan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.suratjalanpembelian'),
        ),
        migrations.AlterField(
            model_name='konversimaster',
            name='KodePenyusun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.penyusun'),
        ),
        migrations.AlterField(
            model_name='penyesuaian',
            name='KodePenyusun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.penyusun'),
        ),
        migrations.AlterField(
            model_name='penyusun',
            name='KodeArtikel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.artikel'),
        ),
        migrations.AlterField(
            model_name='penyusun',
            name='KodeProduk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.produk'),
        ),
        migrations.AlterField(
            model_name='penyusun',
            name='Lokasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.lokasi'),
        ),
        migrations.AlterField(
            model_name='saldoawalartikel',
            name='IDBahanBaku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.artikel'),
        ),
        migrations.AlterField(
            model_name='saldoawalartikel',
            name='IDLokasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.lokasi'),
        ),
        migrations.AlterField(
            model_name='saldoawalbahanbaku',
            name='IDBahanBaku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.produk'),
        ),
        migrations.AlterField(
            model_name='saldoawalbahanbaku',
            name='IDLokasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.lokasi'),
        ),
        migrations.AlterField(
            model_name='transaksigudang',
            name='KodeProduk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.produk'),
        ),
        migrations.AlterField(
            model_name='transaksigudang',
            name='Lokasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.lokasi'),
        ),
        migrations.AlterField(
            model_name='transaksiproduksi',
            name='KodeArtikel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.artikel'),
        ),
        migrations.AlterField(
            model_name='transaksiproduksi',
            name='Lokasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.lokasi'),
        ),
    ]
