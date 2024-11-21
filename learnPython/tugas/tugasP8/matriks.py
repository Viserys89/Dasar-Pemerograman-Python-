n = int(input("Masukan ordo : "))
angka = 1
if n <= 0:
    print("Masukan nilai yang valid!")
else:
    print(f"n = {n}")
    for i in range(n):
        for j in range(n):
            print(angka, end = "  ")
            angka += 1
        print()