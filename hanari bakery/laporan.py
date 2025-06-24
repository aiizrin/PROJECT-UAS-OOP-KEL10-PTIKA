def cetak_laporan_produksi(nama_produk, jumlah_pcs, estimasi, bahan_baku):
    print("=== Laporan Produksi Hanari Bakery ===")
    print(f"Produk       : {nama_produk}")
    print(f"Jumlah       : {jumlah_pcs} pcs")
    print("\n>> Estimasi Keuangan")
    print(f"- Total Pemasukan  : Rp{estimasi['total_pemasukan']:,}")
    print(f"- Total Biaya      : Rp{estimasi['total_biaya']:,}")
    print(f"- Estimasi Profit  : Rp{estimasi['estimasi_profit']:,}")
    
    print("\n>> Bahan Baku yang Dibutuhkan")
    for bahan, jumlah in bahan_baku.items():
        print(f"- {bahan}: {jumlah * jumlah_pcs}")

def simpan_laporan_ke_file(nama_file, nama_produk, jumlah_pcs, estimasi, bahan_baku):
    with open(nama_file, 'w') as f:
        f.write("=== Laporan Produksi Hanari Bakery ===\n")
        f.write(f"Produk       : {nama_produk}\n")
        f.write(f"Jumlah       : {jumlah_pcs} pcs\n")
        f.write("\n>> Estimasi Keuangan\n")
        f.write(f"- Total Pemasukan  : Rp{estimasi['total_pemasukan']:,}\n")
        f.write(f"- Total Biaya      : Rp{estimasi['total_biaya']:,}\n")
        f.write(f"- Estimasi Profit  : Rp{estimasi['estimasi_profit']:,}\n")
        
        f.write("\n>> Bahan Baku yang Dibutuhkan\n")
        for bahan, jumlah in bahan_baku.items():
            f.write(f"- {bahan}: {jumlah * jumlah_pcs}\n")