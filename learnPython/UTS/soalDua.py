sama = 0
gan = 0
while True:
    n = input("Masukkan bilangan bulat positif (atau bilangan negatif untuk berhenti): ")
    try:
        number = int(n)
        if number < 0:
            break 
        if number % 2 == 0:
            sama += number
        else:
            gan+= number
    except ValueError:
        print("Input tidak valid. Silakan masukkan bilangan bulat.")
print(f"Jumlah bilangan genap adalah: {sama}")
print(f"Jumlah bilangan ganjil adalah: {gan}")