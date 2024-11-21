jumlah = 0
data = ""
for angka in range(1, 11):
    data += str(angka)
    if angka == 10:
        data += "="
    else:
        data += "+"
    jumlah += angka
    print(data + str(jumlah))