from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from django.urls import reverse
from datetime import datetime
from . import models
from django.db.models import Sum
from django.http import JsonResponse


# Create your views here.
# RND
def views_artikel(request):
    datakirim = []
    data = models.Artikel.objects.all()
    for item in data:
        print(item)
        detailartikelobj = models.Penyusun.objects.filter(KodeArtikel=item.id).filter(
            Status=1
        )
        print(detailartikelobj)
        if detailartikelobj.exists():
            datakirim.append([item, detailartikelobj[0]])
        else:
            datakirim.append([item, "Belum diset"])
    print(datakirim)
    return render(request, "views_artikel.html", {"data": datakirim})


def tambahdataartikel(request):
    if request.method == "GET":
        return render(request, "tambahdataartikel.html")
    if request.method == "POST":
        # print(dir(request))
        kodebaru = request.POST["kode"]
        keterangan = request.POST["keterangan"]
        data = models.Artikel.objects.filter(KodeArtikel=kodebaru).exists()
        if data:
            messages.error(request, "Kode Artikel sudah ada")
            return redirect("tambahdataartikel")
        else:
            messages.success(request, "Data berhasil disimpan")
            newdataobj = models.Artikel(
                KodeArtikel=kodebaru, keterangan=keterangan
            ).save()
            return redirect("views_artikel")


def updatedataartikel(request, id):
    if request.method == "GET":
        return render(request, "updatedataartikel.html")
    else:
        return redirect("views_artikel")


def deleteartikel(request, id):
    print(id)
    dataobj = models.Artikel.objects.get(id=id)
    dataobj.delete()
    return redirect("views_artikel")


def views_penyusun(request):
    print(request.GET)
    data = request.GET
    if len(request.GET) == 0:
        return render(request, "views_penyusun.html")
    else:
        kodeartikel = request.GET["kodeartikel"]
        try:
            get_id_kodeartikel = models.Artikel.objects.get(KodeArtikel=kodeartikel)
            data = models.Penyusun.objects.filter(KodeArtikel=get_id_kodeartikel.id)
            if data.exists():
                print(data)
                return render(
                    request,
                    "views_penyusun.html",
                    {"data": data, "kodeartikel": get_id_kodeartikel},
                )
            else:
                return render(request, "views_penyusun.html")
        except models.Artikel.DoesNotExist:
            messages.error(request, "Kode Artikel Tidak ditemukan")
            return render(request, "views_penyusun.html")


def tambahdatapenyusun(request, id):
    dataartikelobj = models.Artikel.objects.get(id=id)
    if request.method == "GET":
        dataprodukobj = models.Produk.objects.all()

        return render(
            request,
            "tambahdatapenyusun.html",
            {"kodeartikel": dataartikelobj, "dataproduk": dataprodukobj},
        )
    else:
        print(request.POST)
        kodeproduk = request.POST["kodeproduk"]
        statusproduk = request.POST["Status"]
        if statusproduk == "True":
            statusproduk = True
        else:
            statusproduk = False
        lokasi = request.POST["lokasi"]

        newprodukobj = models.Produk.objects.get(KodeProduk=kodeproduk)
        lokasiobj = models.Lokasi.objects.get(NamaLokasi=lokasi)

        penyusunobj = models.Penyusun(
            Status=statusproduk,
            KodeArtikel=dataartikelobj,
            KodeProduk=newprodukobj,
            Lokasi=lokasiobj,
        )

        konversimasterobj = models.KonversiMaster(KodePenyusun=penyusunobj, Kuantitas=0)
        penyusunobj.save()
        konversimasterobj.save()

        return redirect("penyusun_artikel")


# Update Delete Penyusun belum masuk
def konversi(request):
    data = request.GET
    if len(data) == 0:
        return render(request, "views_konversi.html")
    else:
        kodeartikel = request.GET["kodeartikel"]
        try:
            get_id_kodeartikel = models.Artikel.objects.get(KodeArtikel=kodeartikel)
        except models.Artikel.DoesNotExist:
            messages.error(request, "Data Artikel tidak ditemukan")
            return redirect("konversi")
        data = models.Penyusun.objects.filter(KodeArtikel=get_id_kodeartikel.id)
        if data.exists():
            listdata = []
            for i in data:
                print(i.IDKodePenyusun)
                allowance = models.KonversiMaster.objects.get(
                    KodePenyusun=i.IDKodePenyusun
                )
                listdata.append(
                    [i, allowance, allowance.Kuantitas + allowance.Kuantitas * 0.025]
                )
            print(listdata)
            return render(
                request,
                "views_konversi.html",
                {"data": listdata, "kodeartikel": kodeartikel},
            )
        else:
            return render(request, "views_konversi.html")


def konversimaster_update(request, id):
    dataobj = models.Penyusun.objects.get(IDKodePenyusun=id)
    if request.method == "GET":
        return render(request, "update_konversimaster.html", {"data": dataobj})
    else:
        konversimasterobj = models.KonversiMaster.objects.get(IDKodeKonversiMaster=id)
        print(konversimasterobj)
        konversimasterobj.Kuantitas = float(request.POST["kuantitas"])
        konversimasterobj.save()
        return redirect("konversi")


def konversimaster_delete(request, id):
    dataobj = models.KonversiMaster.objects.get(IDKodeKonversiMaster=id)
    dataobj.Kuantitas = 0
    dataobj.save()
    return redirect("konversi")

'''PURCHASING'''
# READ NOTIF BARANG MASUK PURCHASIN +SPK G+ACC
def notif_barang_purchasing(request) :
    filter_dataobj = models.DetailSuratJalanPembelian.objects.filter(KeteranganACC = False)
    filter_spkobj = models.SPK.objects.filter(KeteranganACC = False)
    return render(request,'Purchasing/notif_purchasing.html',{
    'filterobj' : filter_dataobj,
    'filter_spkobj' :filter_spkobj,
        })    

def verifikasi_data (request,id) :
    verifobj = models.DetailSuratJalanPembelian.objects.get(IDDetailSJPembelian=id)
    if request.method =='GET':
        harga_total = verifobj.Jumlah*verifobj.Harga
        return render(request,'Purchasing/update_verif_data.html',{
        'verifobj' : verifobj ,
        'harga_total' :harga_total,
        })
    else :
        harga_barang = request.POST['harga_barang']
        supplier = request.POST['supplier']
        po_barang = request.POST['po_barang']
        verifobj.KeteranganACC = True
        verifobj.Harga = harga_barang
        verifobj.NoSuratJalan.supplier = supplier
        verifobj.NoSuratJalan.PO = po_barang
        verifobj.save()
        verifobj.NoSuratJalan.save()
        harga_total = verifobj.Jumlah*verifobj.Harga
        return redirect("Purchasing/notif_purchasing")
        
def acc_notif_spk(request,id) :
    accobj = models.SPK.objects.get(NoSPK=id)
    accobj.KeteranganACC = True
    accobj.save()
    return redirect("Purchasing/notif_purchasing")


def barang_masuk(request) :
    if len(request.GET) == 0 :
        return render(request,'Purchasing/masuk_purchasing.html')
    else :
        input_awal = request.GET['awal']
        input_terakhir= request.GET['akhir']
        list_harga_total = []
        
        filtersjb = models.DetailSuratJalanPembelian.objects.filter(NoSuratJalan__Tanggal__range = (input_awal,input_terakhir))
        if len(filtersjb) > 0 :

            for x in filtersjb :
                harga_total = x.Jumlah*x.Harga
                list_harga_total.append(harga_total)
            i = 0
            for item in filtersjb :
                item.harga_total = list_harga_total[i]
                i+=1
            return render(request,'Purchasing/masuk_purchasing.html',{
                'data_hasil_filter':filtersjb,
                'harga_total' :harga_total,
                'input_awal' : input_awal,
                'input_terakhir' :input_terakhir
            })
        else :
            messages.error(request,"Data tidak ditemukan")
            return redirect("Purchasing/barang_masuk")

def update_barang_masuk(request,id,input_awal,input_terakhir) :
    updateobj = models.DetailSuratJalanPembelian.objects.get(IDDetailSJPembelian=id)
    if request.method =='GET':
        harga_total =updateobj.Jumlah*updateobj.Harga
        return render(request,'Purchasing/update_barang_masuk.html',{
        'updateobj' :updateobj ,
        'harga_total' :harga_total,
        })
    else :
        harga_barang = request.POST['harga_barang']
        supplier = request.POST['supplier']
        po_barang = request.POST['po_barang']
        updateobj.Harga = harga_barang
        updateobj.NoSuratJalan.supplier = supplier
        updateobj.NoSuratJalan.PO = po_barang
        updateobj.save()
        updateobj.NoSuratJalan.save()
        harga_total =updateobj.Jumlah*updateobj.Harga
        return redirect(f"Purchasing/barang_masuk?awal={input_awal}&akhir={input_terakhir}")
        # return JsonResponse({'harga_total': harga_total})
def delete_barang_masuk(request,id,input_awal,input_terakhir):
    masukobj = models.DetailSuratJalanPembelian.objects.get(IDDetailSJPembelian=id)
    masukobj.delete()
    return redirect(f"Purchasing/barang_masuk?awal={input_awal}&akhir={input_terakhir}")

def rekap_purchasing(request) :
    return render(request,'Purchasing/rekap_purchasing.html')

def rekap_gudang_purchasing(request) :
    datasjb = models.DetailSuratJalanPembelian.objects.values('KodeProduk','KodeProduk__NamaProduk','KodeProduk__unit','KodeProduk__keterangan').annotate(kuantitas=Sum('Jumlah')).order_by()

    datagudang = models.TransaksiGudang.objects.values('KodeProduk').annotate(kuantitas=Sum('jumlah')).order_by()

    for item in datasjb:
        kode_produk = item['KodeProduk']
        try:
            corresponding_gudang_item = datagudang.get(KodeProduk=kode_produk)
            item['kuantitas'] -= corresponding_gudang_item['kuantitas']
        except models.TransaksiGudang.DoesNotExist:
            pass
        
    
    return render(request,'Purchasing/rekap_gudang_purchasing.html',{
        'datasjb' :datasjb
    })
def rekap_produksi_purchasing(request):
    list_hasil_konversi = []
    list_sisa_produksi = []
    list_kode = []
    
    # Mendapatkan data gudang
    datagudang = models.TransaksiGudang.objects.values(
        'KodeProduk', 
        'KodeProduk__NamaProduk', 
        'KodeProduk__unit', 
        'KodeProduk__keterangan',
    ).annotate(kuantitas=Sum('jumlah')).order_by()
    
    if len(datagudang) <= 0:
        messages.error(request, "Data gudang tidak ditemukan")
        return render(request,"Purchasing/rekap_produksi_purchasing.html")  # Redirect ke halaman kesalahan atau penanganan yang sesuai
        
    # Mendapatkan data produksi
    dataproduksi = models.TransaksiProduksi.objects.filter(Keterangan='mutasi').values('KodeArtikel').annotate(kuantitas=Sum('Jumlah')).order_by()

    for item in dataproduksi:
        kode_artikel = item['KodeArtikel']
        try:
            datakonversi = models.KonversiMaster.objects.filter(IDKodePenyusun__Status=True).filter(IDKodePenyusun__KodeArtikel=kode_artikel)
      
            for konversi in datakonversi:
                hasil_konversi = konversi.Kuantitas * item['kuantitas']
                list_hasil_konversi.append(hasil_konversi)
                kode_produk_konversi = konversi.IDKodePenyusun.KodeProduk_id
                list_kode.append(kode_produk_konversi)
        except models.KonversiMaster.DoesNotExist:
            messages.error(request, "Data konversi tidak ditemukan")
        
    for item2 in datagudang:
        kode_produk = item2['KodeProduk']
        if kode_produk in list_kode:
            index_kode = list_kode.index(kode_produk)
            konversi_produk = list_hasil_konversi[index_kode]
            sisa_produksi = (item2['kuantitas'] - konversi_produk)
            list_sisa_produksi.append(sisa_produksi)
        else:
            pass
    
    i = 0
    for item3 in datagudang:
        item3['sisa_produksi'] = list_sisa_produksi[i]
        i += 1
        
    return render(request, "Purchasing/rekap_produksi_purchasing.html", {
        'datagudang': datagudang,
        'sisa_produksi': sisa_produksi
    })


def read_produk(request) :
    produkobj = models.Produk.objects.all()
    return render(request,'Purchasing/read_produk.html',{
        'produkobj' : produkobj
    })

def create_produk(request) :
    if request.method =='GET':
        return render(request,'Purchasing/create_produk.html')
    else :
        kode_produk = request.POST['kode_produk']
        nama_produk = request.POST['nama_produk']
        unit_produk = request.POST['unit_produk']
        keterangan_produk = request.POST['keterangan_produk']

        new_produk = models.Produk(
            KodeProduk = kode_produk,
            NamaProduk = nama_produk,
            unit = unit_produk,
            keterangan = keterangan_produk,
        )
        new_produk.save()
        return redirect('Purchasing/read_produk')
    
def update_produk(request,id) :
    produkobj = models.Produk.objects.get(pk = id)
    if request.method=='GET':
        return render(request,'Purchasing/update_produk.html',{
            'produkobj' : produkobj
        })
    else :
        kode_produk = request.POST['kode_produk']
        nama_produk = request.POST['nama_produk']
        unit_produk = request.POST['unit_produk']
        keterangan_produk = request.POST['keterangan_produk']
        produkobj.KodeProduk = kode_produk
        produkobj.NamaProduk = nama_produk
        produkobj.unit = unit_produk
        produkobj.keterangan = keterangan_produk
        produkobj.save()
        return redirect('Purchasing/read_produk')
    
def delete_produk(request,id) :
    produkobj = models.Produk.objects.get(KodeProduk = id)
    produkobj.delete()
    return redirect('Purchasing/read_produk')


# Tinggal dibikin gimana biar kodenya yang terkirim pas di reload kode itu lagi yang muncul
def read_po(request) :
    po_objall = models.DetailSuratJalanPembelian.objects.all()
    if request.method == 'GET':
        return render(request,'Purchasing/read_po.html',{
            'po_objall' : po_objall
        })
    else :
        input_po = request.POST['input_po']
        po_obj = models.DetailSuratJalanPembelian.objects.filter(NoSuratJalan__PO = input_po )

        return render(request,'Purchasing/read_po.html',{
            'po_objall' : po_objall,
            'po_obj':po_obj
        })

# Tinggal dibikin gimana biar kodenya yang terkirim pas di reload kode itu lagi yang muncul   
def rekap_harga(request) :

    '''KALAU UNTUK PERHITUNGAN HARGA AVERAGE JANGAN PAKE FILTER TANGGAL, KALAU BUAT DATA DI MASUK BARU PAKE TANGGAL'''
    kodeprodukobj = models.Produk.objects.all() 
    if len(request.GET) == 0 :
        return render(request,'Purchasing/rekap_harga.html',{
            'kodeprodukobj' : kodeprodukobj
        })
    else :
        dict_harga_keluar = {}
        dict_harga_total = {}
        dict_harga_masuk = {}
        dict_harga_average = {}
        list_tanggal = []
        list_supplier = []
        list_kuantitas = []
        list_harga = []
        list_harga_total = []
        kode_produk= request.GET['kode_produk']
        tanggal_awal = request.GET['awal']
        tanggal_akhir = request.GET['akhir']
        # tanggal
        masuk_sjb = models.DetailSuratJalanPembelian.objects.filter(KodeProduk=kode_produk).filter(NoSuratJalan__Tanggal__range=(tanggal_awal,tanggal_akhir))
        masuk_sjb2 = models.DetailSuratJalanPembelian.objects.filter(KodeProduk=kode_produk)
        saldoawalobj = models.SaldoAwalBahanBaku.objects.filter(KodeProduk=kode_produk)
       
        if len(masuk_sjb2)<=0 :
            messages.error(request,"Data tidak ditemukan")
            return redirect("Purchasing/rekap_harga")
        else :
            for item in masuk_sjb2 :
                kodeproduk = item.KodeProduk
                jumlah_masuk = item.Jumlah
                harga_masuk = item.Harga
                harga_total_masuk = jumlah_masuk*harga_masuk
                
                if kodeproduk in dict_harga_total :
                    dict_harga_total[kodeproduk][0] +=harga_total_masuk
                    dict_harga_total[kodeproduk][1] +=jumlah_masuk
                else :
                # dict_harga_total[kodeproduk] = [0]
                    dict_harga_total[kodeproduk] = [harga_total_masuk,jumlah_masuk]
        
            for key in dict_harga_total.keys() :  
                average_harga = dict_harga_total[key][0]/dict_harga_total[key][1]
                dict_harga_average[key] = [average_harga,dict_harga_total[key][1]]
        
            for item in masuk_sjb :
                if item.KodeProduk in dict_harga_masuk :
                    if dict_harga_masuk[item.KodeProduk]['Tanggal'] == item.NoSuratJalan.Tanggal and dict_harga_masuk[item.KodeProduk]['Supplier'] == item.NoSuratJalan.supplier and dict_harga_masuk[item.KodeProduk]['Harga'] == item.Harga :
                        dict_harga_masuk[item.KodeProduk]['Kuantitas'] += item.Jumlah
                    else :
                        harga_masuk = item.Harga
                        jumlah_masuk = item.Jumlah
                        harga_total = jumlah_masuk*harga_masuk
                        dict_harga_masuk[item.KodeProduk]['Tanggal'].append(item.NoSuratJalan.Tanggal)
                        dict_harga_masuk[item.KodeProduk]['Supplier'].append(item.NoSuratJalan.supplier)
                        dict_harga_masuk[item.KodeProduk]['Kuantitas'].append(jumlah_masuk)
                        dict_harga_masuk[item.KodeProduk]['Harga'].append(harga_masuk)
                        dict_harga_masuk[item.KodeProduk]['Harga_Total'].append(harga_total)

                else :
                    harga_masuk = item.Harga
                    jumlah_masuk = item.Jumlah
                    harga_total = jumlah_masuk*harga_masuk
                    dict_harga_masuk[item.KodeProduk] = {}
                    dict_harga_masuk[item.KodeProduk]['Tanggal'] = [item.NoSuratJalan.Tanggal]
                    dict_harga_masuk[item.KodeProduk]['Supplier'] = [item.NoSuratJalan.supplier]
                    dict_harga_masuk[item.KodeProduk]['Kuantitas'] = [jumlah_masuk]
                    dict_harga_masuk[item.KodeProduk]['Harga'] = [harga_masuk]
                    dict_harga_masuk[item.KodeProduk]['Harga_Total'] = [harga_total]

         
        if len(saldoawalobj)<=0 :
            jumlah_saldo= 0
            harga_awal_saldo = 0
            for key in dict_harga_total.keys() :
                harga_total_awal = jumlah_saldo*harga_awal_saldo
                jumlah_total = jumlah_saldo + dict_harga_total[key][1]
            
                harga_total_all = round(harga_total_awal +dict_harga_total[key][0])
        
                average_harga = round(harga_total_all/jumlah_total)
                dict_harga_average[key][0] = average_harga
                dict_harga_average[key][1] = jumlah_total
        else :
            for item2 in saldoawalobj :
                kode_produk2 = item2.KodeProduk
                jumlah_saldo = item2.Jumlah
                harga_awal_saldo = item2.Harga
                jumlah_total = jumlah_saldo + dict_harga_total[key][1]
                harga_total_awal = jumlah_saldo*harga_awal_saldo
                dict_harga_total[key][1]
                harga_total_all = round(harga_total_awal +dict_harga_total[key][0])
                average_harga = round(harga_total_all/jumlah_total)
                dict_harga_average[kode_produk2][0] = average_harga
                dict_harga_average[kode_produk2][1] = jumlah_total
        keluar_sjb = models.TransaksiGudang.objects.filter(KodeProduk=kode_produk).filter(tanggal__range =(tanggal_awal,tanggal_akhir)).filter(jumlah__gt=0)

        list_jumlah = []
        for item in keluar_sjb :
            list_jumlah.append(item.jumlah)
        sum_jumlah = sum(list_jumlah)

        for item3 in keluar_sjb :
            kode_produk3 = item3.KodeProduk
            dict_harga_keluar[kode_produk3] = [0,0,0,0]

        for item4 in keluar_sjb :
            kode_produk4 = item4.KodeProduk
            if kode_produk4 in dict_harga_total:
                harga_keluar = round(dict_harga_average[kode_produk4][0]*sum_jumlah)
                dict_harga_keluar[kode_produk4][0] = item4.tanggal
                dict_harga_keluar[kode_produk4][1] = sum_jumlah
                dict_harga_keluar[kode_produk4][2] = dict_harga_average[kode_produk4][0]
                dict_harga_keluar[kode_produk4][3] = harga_keluar
            else :
                continue
        
        for key in dict_harga_masuk.keys() :
            list_tanggal = dict_harga_masuk[key]['Tanggal']
            list_supplier =dict_harga_masuk[key]['Supplier']
            list_kuantitas = dict_harga_masuk[key]['Kuantitas']
            list_harga = dict_harga_masuk[key]['Harga']
            list_harga_total = dict_harga_masuk[key]['Harga_Total']

    
        tanggal = 0
        supplier = 0
        kuantitas = 0
        harga = 0
        harga_total_1= 0

        i = 0
        for item in masuk_sjb :
            item.tanggal = list_tanggal[i]
            item.supplier = list_supplier[i]
            item.kuantitas = list_kuantitas[i]
            item.harga = list_harga[i]
            item.harga_total_1 = list_harga_total[i]
            i+=1

        return render(request,'Purchasing/rekap_harga.html',{
            'kodeprodukobj' : kodeprodukobj,
            'masuk_sjb':masuk_sjb,
            'harga_masuk' : dict_harga_masuk,
            'harga_keluar' :dict_harga_keluar,
            'harga_total': dict_harga_total,
            'tanggal' : tanggal,
            'supplier' : supplier,
            'kuantitas' : kuantitas,
            'harga' : harga,
            'harga_total_1' : harga_total_1,
            'awal' : tanggal_awal,
            'akhir' :tanggal_akhir
        })
    

