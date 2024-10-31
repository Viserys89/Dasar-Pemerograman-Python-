# Nama : Mukhammad Vicky
# NIM : 2404853
# Kelas : RPL 1 C
student_info = {
    "Alice": {"Age" : 20, "Major" : "Computer Science"},
    "Bob": {"Age" : 21, "Major" : "Mathematics"},
    "Charlie": {"Age" : 19, "Major" : "Physics"},
}
nama_siswa = input("Input nama siswa : ")
if nama_siswa in student_info:
    age = student_info[nama_siswa]["Age"]
    major = student_info[nama_siswa]["Major"]
    print(f"Umur {nama_siswa} adalah {age} dan prodi nya adalah {major}.")
else:
    print(f"Tidak ada siswa dengan nama {nama_siswa}.")