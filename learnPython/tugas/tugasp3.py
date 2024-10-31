""""
Nama : Mukhammad Vicky
NIM : 2404853
Kelas : RPL 1 C
"""

tupleKelas = ("Akmal", "Adzril", "Denis")
listKelas = list(tupleKelas)
listKelas.insert(1, "Vicky")
tupleKelas = tuple(listKelas)
print(tupleKelas)

tupleKelas2 = ("Akmal", "Adzril", "Denis")
listKelas2 = list(tupleKelas2)
listKelas2.append("Vicky")
tupleKelas2 = tuple(listKelas2)
print(tupleKelas)

tupleKelas3 = ("Akmal", "Adzril", "Denis")
listKelas3 = list(tupleKelas3)
listKelas3.pop(0)
tupleKelas3 = tuple(listKelas3)
print(tupleKelas3)