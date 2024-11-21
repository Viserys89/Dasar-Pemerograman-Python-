input_nilai = input("Masukkan nilai-nilai yang dipisahkan dengan koma: ")
rata_rata = sum(float(nilai) for nilai in input_nilai.split(',')) / len(input_nilai.split(','))
print(f"Rata-ratanya adalah {rata_rata}")