# Import modul-modul (setiap modul bisa dikembangkan oleh anggota tim berbeda)
from produksi import ProduksiManager
from bahan_baku import BahanBakuManager
from profit import ProfitEstimator
from produk import ProdukManager

def main():
    print("=== Selamat Datang di Sistem Manajemen Hanari Bakery ===")

    # Inisialisasi modul
    produksi = ProduksiManager()
    bahan_baku = BahanBakuManager()
    profit = ProfitEstimator()
    produk = ProdukManager()
    
    while True:
        print("\nMenu Utama:")
        print("1. Kelola Produksi")
        print("2. Kelola Bahan Baku")
        print("3. Lihat & Update Produk")
        print("4. Estimasi Profit")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            produksi.menu_produksi()
        elif pilihan == "2":
            bahan_baku.menu_bahan_baku()
        elif pilihan == "3":
            produk.menu_produk()
        elif pilihan == "4":
            profit.menu_profit()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem Hanari Bakery!")
            break
        else:
            print("Pilihan tidak valid, silakan ulangi.")

if __name__ == "__main__":
    main()