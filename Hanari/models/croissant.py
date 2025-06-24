from produk import Produk

class Croissant(Produk):
    def tampilkan_info(self):
        print(f"\n[{self.kode}] Croissant")
        for bahan, jumlah in self.bahan_baku.items():
            print(f"    - {bahan}: {jumlah}")
        print(f"  Biaya Produksi (per {self.jumlah_n} pcs): Rp{self.biaya_produksi}")
        print(f"  Harga Jual      (per {self.jumlah_n} pcs): Rp{self.harga_jual}")

    def simulasi_produksi(self):
        print("\nProduksi Croissant:")
        print("1. Pengadonan")
        print("2. Pengembangan (fermentasi)")
        print("3. Pemanggangan")