class EstimasiProfit:
    def hitung_profit(self, produk, jumlah_produksi):
        try:
            rasio = jumlah_produksi / produk.jumlah_n
            total_biaya = rasio * produk.biaya_produksi
            total_penjualan = rasio * produk.harga_jual
            profit = total_penjualan - total_biaya

            print(f"\nEstimasi Profit untuk {jumlah_produksi} pcs:")
            print(f"  Total Biaya     : Rp{int(total_biaya)}")
            print(f"  Total Penjualan : Rp{int(total_penjualan)}")
            print(f"  Profit          : Rp{int(profit)}\n")

        except ZeroDivisionError:
            print("Jumlah produk (n pcs) tidak boleh 0.")
        except Exception as e:
            print("Terjadi kesalahan dalam perhitungan profit:", e)