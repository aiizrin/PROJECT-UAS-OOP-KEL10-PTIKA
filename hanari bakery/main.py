from models.produk import RotiManis, Croissant, ButterCookies, Muffin
from models.bahan_baku import BahanBaku
from estimasiprofit import hitung_profit

produk_list = []
stok_bahan = BahanBaku()

def tambah_produk():
    print("\n=== Tambah Produk ===")
    print("1. Roti Manis\n2. Croissant\n3. Butter Cookies\n4. Muffin")
    pilihan = input("Pilih jenis produk: ")
    nama = input("Nama produk: ")
    kode = input("Kode produk: ")
    bahan = {}
    print("Masukkan bahan (ketik 'selesai' untuk berhenti):")
    while True:
        nama_bahan = input("Bahan: ")
        if nama_bahan == 'selesai':
            break
        jumlah = int(input("Jumlah: "))
        bahan[nama_bahan] = jumlah
    biaya = int(input("Biaya produksi per-n pcs: "))
    harga = int(input("Harga jual per-n pcs: "))

    if pilihan == '1':
        produk = RotiManis(kode, nama, bahan, biaya, harga)
    elif pilihan == '2':
        produk = Croissant(kode, nama, bahan, biaya, harga)
    elif pilihan == '3':
        produk = ButterCookies(kode, nama, bahan, biaya, harga)
    elif pilihan == '4':
        produk = Muffin(kode, nama, bahan, biaya, harga)
    else:
        print("Pilihan tidak valid.")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan.")

def tampilkan_produk():
    print("\n=== Daftar Produk ===")
    if not produk_list:
        print("Belum ada produk.")
        return
    for p in produk_list:
        p.tampilkan_info()

def estimasi_profit():
    tampilkan_produk()
    kode = input("Masukkan kode produk: ")
    jumlah = int(input("Masukkan jumlah produksi (n): "))
    produk = next((p for p in produk_list if p.kode == kode), None)
    if produk:
        profit = hitung_profit(produk, jumlah)
        print(f"Estimasi Profit: Rp{profit}")
    else:
        print("Produk tidak ditemukan.")

def simulasi_produksi():
    tampilkan_produk()
    kode = input("Masukkan kode produk: ")
    produk = next((p for p in produk_list if p.kode == kode), None)
    if produk:
        if stok_bahan.cukup(produk.bahan_baku):
            print("Bahan cukup, memulai produksi...")
            produk.proses_produksi()
            stok_bahan.pakai_bahan(produk.bahan_baku)
        else:
            print("Bahan tidak mencukupi.")
    else:
        print("Produk tidak ditemukan.")

def isi_bahan_baku():
    print("\n=== Isi Bahan Baku ===")
    while True:
        nama = input("Nama bahan (atau 'selesai'): ")
        if nama == 'selesai':
            break
        jumlah = int(input("Jumlah: "))
        stok_bahan.tambah_bahan(nama, jumlah)

def main():
    while True:
        print("\n--- HANARI BAKERY ---")
        print("1. Tambah Produk")
        print("2. Tampilkan Produk")
        print("3. Estimasi Profit")
        print("4. Simulasi Produksi")
        print("5. Isi Bahan Baku")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            tambah_produk()
        elif pilihan == '2':
            tampilkan_produk()
        elif pilihan == '3':
            estimasi_profit()
        elif pilihan == '4':
            simulasi_produksi()
        elif pilihan == '5':
            isi_bahan_baku()
        elif pilihan == '6':
            break
        else:
            print("Menu tidak valid.")

if _name_ == "_main_":
    main() 
