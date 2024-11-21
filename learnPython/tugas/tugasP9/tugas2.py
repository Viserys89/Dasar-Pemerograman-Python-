def login():
    pw = "Latihan"
    coba = 3
    for Coba in range(coba):
        password = input("Masukkan password: ")
        if password == pw:
            print("Login berhasil!")
            return
        print(f"Login gagal. Anda memiliki {coba - Coba - 1} kesempatan lagi.")

    print("Anda telah mencoba 3 kali. Anda telah terblokir.")
username = input("Masukkan username: ")
login()