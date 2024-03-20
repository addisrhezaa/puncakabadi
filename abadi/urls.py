from django.urls import path
from . import views

urlpatterns = [
    path("artikel", views.views_artikel, name="views_artikel"),
    path("tambahdataartikel", views.tambahdataartikel, name="tambahdataartikel"),
    path("updateartikel/<str:id>", views.updatedataartikel, name="update_artikel"),
    path("deleteartikel/<str:id>", views.deleteartikel, name="delete_artikel"),
    path("penyusunartikel", views.views_penyusun, name="penyusun_artikel"),
    path(
        "tambahdatapenyusun/<str:id>",
        views.tambahdatapenyusun,
        name="tambah_data_penyusun",
    ),
    path("konversi", views.konversi, name="konversi"),
    path(
        "Updatekonversi/<str:id>",
        views.konversimaster_update,
        name="update_data_konversi_master",
    ),
    path(
        "Deletekonversi/<str:id>",
        views.konversimaster_delete,
        name="delete_data_konversi_master",
    ),
    # notif purchasing +spk
    path("Purchasing/notif_purchasing",views.notif_barang_purchasing,name="notif_purchasing"),
    path("Purchasing/update_verif_purchasing/<str:id>",views.verifikasi_data,name ="update_verif_purchasing"),
    path("Purchasing/acc_spk/<str:id>",views.acc_notif_spk,name="acc_spk"),

    # barang_masuk
    path("Purchasing/barang_masuk",views.barang_masuk,name="barang_masuk"),
    path("Purchasing/update_barang_masuk/<str:id>/<str:input_awal>/<str:input_terakhir>",views.update_barang_masuk,name ="update_barang_masuk"),
    path("Purchasing/delete_barang_masuk/<str:id>/<str:input_awal>/<str:input_terakhir>",views.delete_barang_masuk,name ="delete_barang_masuk"),

    # rekap purchasing(gudang+produksi)
    path("Purchasing/rekap_purchasing",views.rekap_purchasing,name = "rekap_purchasing"),

    path("Purchasing/rekap_gudang_purchasing",views.rekap_gudang_purchasing,name="rekap_gudang_purchasing"),
    path("Purchasing/rekap_produksi_purchasing",views.rekap_produksi_purchasing,name="rekap_produksi_purchasing"),
    # CRUD PRODUK
    path("Purchasing/read_produk",views.read_produk,name="read_produk"),
    path("Purchasing/create_produk",views.create_produk,name="create_produk"),
    path("Purchasing/update_produk/<str:id>",views.update_produk,name="update_produk"),
    path("Purchasing/delete_produk/<str:id>",views.delete_produk,name="delete_produk"),

    # R PO
    path("Purchasing/read_po",views.read_po,name="read_po"),
    path("Purchasing/rekap_harga",views.rekap_harga,name="rekap_harga")
]

