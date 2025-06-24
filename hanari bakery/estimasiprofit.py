def hitung_profit(produk, jumlah):
    total_biaya = produk.biaya_produksi * jumlah
    total_penjualan = produk.harga_jual * jumlah
    return total_penjualan - total_biaya
