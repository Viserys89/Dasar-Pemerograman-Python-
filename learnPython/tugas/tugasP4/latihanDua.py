# Nama : Mukhammad Vicky
# NIM : 2404853
# Kelas : RPL 1 C
students = {
    'Alice': 'computer science',
    'Bob': 'mathematics',
    'Charlie': 'physics',
    'David': 'computer science',
    'Eve': 'mathematics'
}
jurusan = input("Masukan jurusan: ").lower()
jumlahSiswa = sum(1 for prodi in students.values() if prodi == jurusan)
if jumlahSiswa > 0:
    print(f"Prodi {jurusan} sebanyak {jumlahSiswa}")
else:
    print(f"Tidak ada prodi {jurusan}")
