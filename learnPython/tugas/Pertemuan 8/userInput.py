# Nama : Mukhammad Vicky
# NIM : 2404853
# Kelas : RPL 1 C
number = 0
jumlah = 0
while number >= 0:
    number = int(input("Masukan angka (bila negatif akan berhenti) : "))
    if number <= 0:
        print("Masukan angka yang valid!")
    else:
        jumlah += number
        continue
    print(f"Total jumlah yang kamu input adalah : {jumlah}") 