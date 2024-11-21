def deretFibonacci(n):
    deret = [0 ,1]
    while len(deret) < n:
        deret.append(deret[-1] + deret[-2])
    return deret
jumlah = int(input("Masukan jumlah deret fibonacci : "))
deret = deretFibonacci(jumlah)
print(deret)