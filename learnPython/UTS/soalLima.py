count = 0
sblm = None
total = 0
while count < 3:
    try:
        baru= int(input("Input bilangan: "))
        if sblm is not None:
            if baru> sblm:
                total += baru
                count = 0
            else:
                count += 1
        sblm = baru
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")
print(f"Hasil penjumlahan nilai yang membesar: {total}")