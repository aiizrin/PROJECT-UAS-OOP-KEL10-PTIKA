class ButterCookies(Produk):
    def tampilkan_info(self):
        print(f"\n[{self.kode}] Butter Cookies")
        for bahan, jumlah in self.bahan_baku.items():
            print(f"    - {bahan}: {jumlah}")
        print(f"  Biaya Produksi (per {self.jumlah_n} pcs): Rp{self.biaya_produksi}")
        print(f"  Harga Jual      (per {self.jumlah_n} pcs): Rp{self.harga_jual}")

    def simulasi_produksi(self):
        print("\nProduksi Butter Cookies:")
        print("1. Pengadonan")
        print("2. Pemanggangan")
        print("3. Penambahan topping")
