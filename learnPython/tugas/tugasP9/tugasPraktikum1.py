import math
def volume_tabung(jarijari, tinggi):
    return math.pi * jarijari ** 2 * tinggi

jarijari = float(input("Masukkan nilai jari-jari: "))
tinggi = float(input("Masukkan nilai tinggi: "))

if jarijari >= 0 and tinggi >= 0:
    hasil = volume_tabung(jarijari, tinggi)
    print(f"Volume tabung adalah: {hasil:.2f}")
else:
    print("Jari-jari dan tinggi harus bilangan positif.")