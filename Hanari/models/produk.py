from abc import ABC, abstractmethod

class Produk(ABC):
    def __init__(self, kode, nama, bahan_baku, biaya_produksi, harga_jual, jumlah_n):
        self.kode = kode
        self.nama = nama
        self.bahan_baku = bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual
        self.jumlah_n = jumlah_n

    @abstractmethod
    def tampilkan_info(self):
        pass

    @abstractmethod
    def simulasi_produksi(self):
        pass
