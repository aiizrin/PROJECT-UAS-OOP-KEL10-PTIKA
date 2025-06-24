class Produk(ProsesProduksi):
    def __init__(self, nama, kode, bahan_baku, biaya, harga_jual, n_pcs):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku  
        self.biaya = biaya
        self.harga_jual = harga_jual
        self.n_pcs = n_pcs

    def tampilkan_info(self):
        print(f"\n[{self.kode}] {self.nama}")
        print("Bahan Baku:")
        for bahan, jumlah in self.bahan_baku.items():
            print(f"- {bahan}: {jumlah}")
        print(f"Biaya Produksi (per {self.n_pcs} pcs): Rp{self.biaya}")
        print(f"Harga Jual (per {self.n_pcs} pcs): Rp{self.harga_jual}")

    def estimasi_profit(self, jumlah):
        rasio = jumlah / self.n_pcs
        total_biaya = self.biaya * rasio
        total_jual = self.harga_jual * rasio
        return total_jual - total_biaya

    def kembangkan(self):
        pass 

class RotiManis(Produk):
    def adon(self): print("Mengadon adonan roti manis...")
    def kembangkan(self): print("Proses pengembangan roti manis...")
    def panggang(self): print("Memanggang roti manis...")
    def topping(self): print("Menambahkan topping roti manis...")

class Croissant(Produk):
    def adon(self): print("Mengadon croissant dengan lipatan butter...")
    def kembangkan(self): print("Proses fermentasi croissant...")
    def panggang(self): print("Memanggang croissant...")
    def topping(self): print("Menambahkan topping croissant..."

class ButterCookies(Produk):
    def adon(self): print("Mengadon butter cookies...")
    def panggang(self): print("Memanggang butter cookies...")
    def topping(self): print("Menaburkan topping cookies...")

class Muffin(Produk):
    def adon(self): print("Mengadon adonan muffin...")
    def kembangkan(self): print("Proses pengembangan muffin...")
    def panggang(self): print("Memanggang muffin...")
    def topping(self): print("Menambahkan topping muffin...")
