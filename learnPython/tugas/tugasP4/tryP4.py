setA = {"akmal", "denis", "yassir", "gassan"}
for item in setA:
    print(item)
setA.add("adzril")
setB = {"Mahesa", "Wisnu"}
setC = setA.union(setB)
setA.update(setB)
# print(setA)
# print(setC)
setA.intersection_update(setB)
print(setA)

# dictionary
Kucing = {
    "nama" : "Wiskey",
    "umur" : "2 Bulan",
    "ras" : "Persian",
    "Jantan" : True,
    "Jelek" : False,
    "Hobi" : ["Makan", "Tidur"]
}
print(Kucing)
print(len(Kucing))
print(Kucing["nama"])
print(Kucing.get("ras"))
print(Kucing.keys())
Kucing.update({"umur" : 2})
Kucing.update({"Warna" : ["putih", "hitam"]})
print(Kucing)
