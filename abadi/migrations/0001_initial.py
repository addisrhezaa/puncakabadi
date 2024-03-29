# Generated by Django 4.1.4 on 2024-03-06 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KodeArtikel', models.CharField(max_length=20)),
                ('keterangan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lokasi',
            fields=[
                ('IDLokasi', models.AutoField(primary_key=True, serialize=False)),
                ('NamaLokasi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('KodeProduk', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('NamaProduk', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=20)),
                ('keterangan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SPK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoSPK', models.CharField(max_length=255)),
                ('Tanggal', models.DateField()),
                ('Keterangan', models.CharField(max_length=255)),
                ('KeteranganACC', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SPPB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoSPPB', models.CharField(max_length=255)),
                ('Tanggal', models.DateField()),
                ('Keterangan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SuratJalanPembelian',
            fields=[
                ('NoSuratJalan', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Tanggal', models.DateField()),
                ('supplier', models.CharField(max_length=255)),
                ('PO', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TransaksiProduksi',
            fields=[
                ('idTransaksiProduksi', models.AutoField(primary_key=True, serialize=False)),
                ('Tanggal', models.DateField()),
                ('Jumlah', models.IntegerField()),
                ('Keterangan', models.CharField(max_length=255)),
                ('Jenis', models.CharField(max_length=20)),
                ('KodeArtikel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.artikel')),
                ('Lokasi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.lokasi')),
            ],
        ),
        migrations.CreateModel(
            name='TransaksiGudang',
            fields=[
                ('IDDetailTransaksiGudang', models.AutoField(primary_key=True, serialize=False)),
                ('keterangan', models.CharField(max_length=20)),
                ('jumlah', models.IntegerField()),
                ('tanggal', models.DateField()),
                ('KeteranganACC', models.BooleanField()),
                ('KodeProduk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.produk')),
                ('Lokasi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.lokasi')),
            ],
        ),
        migrations.CreateModel(
            name='SaldoAwalBahanBaku',
            fields=[
                ('IDSaldoAwalBahanBaku', models.AutoField(primary_key=True, serialize=False)),
                ('Jumlah', models.IntegerField()),
                ('Harga', models.FloatField()),
                ('IDBahanBaku', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.produk')),
                ('IDLokasi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.lokasi')),
            ],
        ),
        migrations.CreateModel(
            name='SaldoAwalArtikel',
            fields=[
                ('IDSaldoAwalBahanBaku', models.AutoField(primary_key=True, serialize=False)),
                ('Jumlah', models.IntegerField()),
                ('IDBahanBaku', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.artikel')),
                ('IDLokasi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.lokasi')),
            ],
        ),
        migrations.CreateModel(
            name='Penyusun',
            fields=[
                ('IDKodePenyusun', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.BooleanField()),
                ('KodeArtikel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.artikel')),
                ('KodeProduk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.produk')),
                ('Lokasi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.lokasi')),
            ],
        ),
        migrations.CreateModel(
            name='Penyesuaian',
            fields=[
                ('IDPenyesuaian', models.AutoField(primary_key=True, serialize=False)),
                ('TanggalMulai', models.DateField()),
                ('TanggalAkhir', models.DateField()),
                ('KodePenyusun', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.penyusun')),
            ],
        ),
        migrations.CreateModel(
            name='KonversiMaster',
            fields=[
                ('IDKodeKonversiMaster', models.AutoField(primary_key=True, serialize=False)),
                ('Kuantitas', models.FloatField()),
                ('KodePenyusun', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.penyusun')),
            ],
        ),
        migrations.CreateModel(
            name='DetailSuratJalanPembelian',
            fields=[
                ('IDDetailSJPembelian', models.AutoField(primary_key=True, serialize=False)),
                ('Jumlah', models.IntegerField()),
                ('KeteranganACC', models.BooleanField()),
                ('Harga', models.FloatField()),
                ('KodeProduk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.produk')),
                ('NoSuratJalan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.suratjalanpembelian')),
            ],
        ),
        migrations.CreateModel(
            name='DetailSPPB',
            fields=[
                ('IDDetailSPPB', models.AutoField(primary_key=True, serialize=False)),
                ('Jumlah', models.IntegerField()),
                ('NoSPK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.spk')),
                ('NoSPPB', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.sppb')),
            ],
        ),
        migrations.CreateModel(
            name='DetailSPK',
            fields=[
                ('IDDetailSPK', models.AutoField(primary_key=True, serialize=False)),
                ('Jumlah', models.IntegerField()),
                ('KodeArtikel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.artikel')),
                ('NoSPK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.spk')),
            ],
        ),
        migrations.CreateModel(
            name='DetailKonversiProduksi',
            fields=[
                ('IDDetailKonversiProduksi', models.AutoField(primary_key=True, serialize=False)),
                ('kuantitas', models.FloatField()),
                ('KodePenyesuaian', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.penyesuaian')),
            ],
        ),
    ]
