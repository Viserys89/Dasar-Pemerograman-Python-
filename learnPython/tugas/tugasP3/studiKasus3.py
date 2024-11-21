# Nama : Mukhammad Vicky
# NIM : 2404853
# Kelas : RPL 1 C

listBuah = ["Apel", "Jeruk", "Ceri", "Durian", "Apel", "Mangga"]
listBuah[2] = "Cherry"
index = int(input("ingin menambahkan ke index berapa? "))
buah = str(input("Masukan buah yang ingin ditambahkan "))
listBuah[index] = buah
listBuah.sort() 
print(listBuah)