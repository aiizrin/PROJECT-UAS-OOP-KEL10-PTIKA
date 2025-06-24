class BahanBaku:
    def _init_(self):
        self.data = {}  # nama_bahan -> stok

    def tambah_bahan(self, nama, jumlah):
        if nama in self.data:
            self.data[nama] += jumlah
        else:
            self.data[nama] = jumlah

    def tampilkan(self):
        print("\nStok Bahan Baku:")
        for nama, jumlah in self.data.items():
            print(f"- {nama}: {jumlah}")

    def cukup(self, bahan_dibutuhkan):
        for bahan, jumlah in bahan_dibutuhkan.items():
            if self.data.get(bahan, 0) < jumlah:
                return False
        return True

    def pakai_bahan(self, bahan_dibutuhkan):
        if self.cukup(bahan_dibutuhkan):
            for bahan, jumlah in bahan_dibutuhkan.items():
                self.data[bahan] -= jumlah
            return True
        return False
