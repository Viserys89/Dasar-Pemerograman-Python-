"""
Nama : Mukhammad Vicky
NIM : 2404853
Kelas : RPL 1 C
"""
mobil = {
    "Merk" : "Honda",
    "Tipe" : "HRV",
    "Tahun" : "2018",
    "Warna" : "Hitam",
    "NoPolisi" : "D 1234 ABC",
    "Bensin" : "Pertalite",
    "Tranmisi" : "Manual",
}
print(f"mobil lama Pak Oki adalah :\n {mobil}")
print("Masukan Informasi detail mobil baru : ")
merkB = input("Merk : ")
tipeB = input("Tipe : ")
tahunB = input("Tahun : ")
warnaB = input("Warna : ")
nopolisiB = input("No polisi : ")
bensinB = input("Bensin : ")
transmisiB = input("Transmisi : ")
mobil.update({"Merk" : merkB, "Tipe": tipeB, "Tahun" : tahunB, "Warna" : warnaB, "NoPolisi" : nopolisiB, "Bensin" : bensinB, "Transmisi" : transmisiB})
print(mobil)