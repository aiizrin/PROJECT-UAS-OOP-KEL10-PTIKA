from Hanari.models.produk import Produk

class RotiManis(Produk):
    def tampilkan_info(self):
        print(f"\n[{self.kode}] Roti Manis")
        for bahan, jumlah in self.bahan_baku.items():
            print(f"    - {bahan}: {jumlah}")
        print(f"  Biaya Produksi (per {self.jumlah_n} pcs): Rp{self.biaya_produksi}")
        print(f"  Harga Jual      (per {self.jumlah_n} pcs): Rp{self.harga_jual}")

    def simulasi_produksi(self):
        print("\nProduksi Roti Manis:")
        print("1. Pengadonan")
        print("2. Pengembangan (fermentasi)")
        print("3. Pemanggangan")
