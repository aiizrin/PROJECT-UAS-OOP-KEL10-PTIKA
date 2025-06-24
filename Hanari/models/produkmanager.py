from Hanari.models.buttercookies import ButterCookies
from Hanari.models.croissant import Croissant
from Hanari.models.muffin import Muffin
from Hanari.models.rotimanis import RotiManis

class ProdukManager:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self):
        kode = input("Kode produk  : ").upper()
        jenis = input("Jenis produk (roti manis / croissant / cookies / muffin): ").lower()
        nama = input("Nama produk  : ").title()

        bahan_baku = {}
        print("Masukkan bahan baku (selesai untuk berhenti):")
        while True:
            bahan = input("  Bahan: ")
            if bahan.lower() == 'selesai':
                break
            jumlah = float(input("  Jumlah: "))
            bahan_baku[bahan] = jumlah

        biaya = int(input("Biaya produksi (Rp): "))
        harga = int(input("Harga jual (Rp): "))
        jumlah_n = int(input("Jumlah pcs dari resep ini: "))

        if jenis == "roti manis":
            produk = RotiManis(kode, nama, bahan_baku, biaya, harga, jumlah_n)
        elif jenis == "croissant":
            produk = Croissant(kode, nama, bahan_baku, biaya, harga, jumlah_n)
        elif jenis == "cookies":
            produk = ButterCookies(kode, nama, bahan_baku, biaya, harga, jumlah_n)
        elif jenis == "muffin":
            produk = Muffin(kode, nama, bahan_baku, biaya, harga, jumlah_n)
        else:
            print("Jenis produk tidak dikenali.")
            return

        self.daftar_produk.append(produk)
        print("Produk berhasil ditambahkan.\n")

    def tampilkan_produk(self):
        if not self.daftar_produk:
            print("Belum ada produk.")
        else:
            for p in self.daftar_produk:
                p.tampilkan_info()

    def cari_produk(self, kode):
        for p in self.daftar_produk:
            if p.kode == kode:
                return p
        return None