input_user = input("Masukan 3 digit nim terakhir: ")

if len(input_user) == 3 and input_user.isdigit():
    angka = int(input_user)
    if 1 <= angka <= 50:
        kelas = "K1" if angka % 2 != 0 else "K2"
    elif 51 <= angka <= 100:
        kelas = "K3" if angka % 2 != 0 else "K4"
    elif 101 <= angka <= 150:
        kelas = "K5" if angka % 2 != 0 else "K6"
    elif angka > 150:
        kelas = "K7" if angka % 2 != 0 else "K8"
    else:
        kelas = None
    if kelas:
        print(f"Kelas: {kelas}")
    else:
        print("NIM tidak valid")
else:
    print("NIM tidak valid")