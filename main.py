
from Hanari.models.produkmanager import ProdukManager
from Hanari.models.estimasi import EstimasiProfit

def tampilkan_menu():
    manajer = ProdukManager()
    profit_calculator = EstimasiProfit()

    while True:
        print("\nMenu:")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Simulasi Produksi")
        print("4. Estimasi Profit")
        print("5. Keluar")

        pilih = input("Pilih: ")
        if pilih == "1":
            manajer.tambah_produk()
        elif pilih == "2":
            manajer.tampilkan_produk()
        elif pilih == "3":
            kode = input("Kode produk: ").upper()
            produk = manajer.cari_produk(kode)
            if produk:
                produk.simulasi_produksi()
            else:
                print("Produk tidak ditemukan.")
        elif pilih == "4":
            kode = input("Kode produk: ").upper()
            produk = manajer.cari_produk(kode)
            if produk:
                try:
                    jumlah = int(input("Jumlah produksi (pcs): "))
                    profit_calculator.hitung_profit(produk, jumlah)
                except ValueError:
                    print("Jumlah harus angka.")
            else:
                print("Produk tidak ditemukan.")
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    tampilkan_menu()
