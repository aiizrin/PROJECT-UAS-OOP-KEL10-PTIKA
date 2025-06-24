def hitung_estimasi_profit(harga_jual, biaya_produksi, jumlah_pcs):
    total_pemasukan = harga_jual * jumlah_pcs
    total_biaya = biaya_produksi * jumlah_pcs
    profit = total_pemasukan - total_biaya
    return {
        "total_pemasukan": total_pemasukan,
        "total_biaya": total_biaya,
        "estimasi_profit": profit
    }
