n = int(input("Masukan jumlah : "))
for i in range (n, 0, -1):
    angka = n
    print(f'''
{i} bebek kecil berenang
Menyusuri sungai yang deras
Induknya mencari kwek kwek kwek
Hanya ekor yang pulang''')
    if i == 1:
        print("Dan semua bebek kecil pulang, aha!")
    else:
        print(f"Hanya {i-1} ekor yang pulang\n")