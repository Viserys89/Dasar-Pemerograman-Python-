"""
Nama : Mukhammad Vicky
NIM : 2404853
Kelas : RPL 1 C
"""
barangNabila = ["T-Shirt", "Blouse", "Kemeja", "Celana Panjang", "Rok", "Baju Renang", "Tas", "Topi", "Sepatu","Sendal"]
print(f"Barang jualan Nabila pada bulan Juli berjumlah {len(barangNabila)}. Barangnya antara lain :\n{barangNabila}")
barangNabila[5] = "Gamis"
barangBaru = ["Ikat Rambut", "Kerudung"]
barangNabila.extend(barangBaru)
print(f"Barang jualan Nabila pada bulan ini berjumlah {len(barangNabila)}. Barangnya antara lain :\n {barangNabila}")