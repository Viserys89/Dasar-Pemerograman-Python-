"""
nama = "Mukhammad Vicky"
nim = "2404853"
kelas = "RPL 1 C"
"""
panjang = 8
tinggi = 4
lebar = 10
luasPermu = 2 * (panjang * tinggi) + 2 * (lebar * tinggi)
print(f"Luas permukaan dinding adalah {luasPermu} m²")
biaya_per_m2 = 520000
total_biaya = biaya_per_m2 * luasPermu
print(f"Biaya pembuatan bangunan dengan tinggi {tinggi} meter dengan panjang {panjang} meter dan lebar {lebar} meter adalah Rp. {total_biaya:,.0f}" .replace(',', '.'))
