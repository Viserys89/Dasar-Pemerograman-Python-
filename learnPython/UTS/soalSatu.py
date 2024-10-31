username= "loginUTS"
pw = "rpl2024"
coba = 3
for Coba in range(coba):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == username and password == pw:
        print("Login berhasil! Selamat datang di aplikasi.")
        break
    else:
        print(f"Login gagal. Kesempatan tersisa: {coba - Coba - 1}")
if Coba == coba - 1:
    print("Anda telah menggunakan semua kesempatan. Akses ditolak.")