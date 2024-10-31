N = int(input("Masukkan nilai N: "))
prima = 0
if N <= 0:
    print("N harus lebih dari nol!")
else:
    for i in range(N):
        bil = int(input(f"Masukkan bilangan ke-{i + 1}: "))
        if bil > 1:
            is_prima = True
            for j in range(2, int(bil**0.5) + 1):
                if bil % j == 0:
                    is_prima = False
                    break
            if is_prima:
                prima += bil
        else:
            print("Tidak ada item list yang bilangan prima")
    if prima == 0:
        print("Tidak ada item list yang bilangan prima")
    else:
        print(f"Jumlah bilangan prima adalah: {prima}")