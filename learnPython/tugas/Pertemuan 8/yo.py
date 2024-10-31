a = int(input("masukan : "))
value = 1
for i in range (a):
    row = []
    for j in range(a):
        row.append(value)
        value += 1
    print(row)