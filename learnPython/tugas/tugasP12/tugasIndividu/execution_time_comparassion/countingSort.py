# Nama : Mukhammad Vicky
# NIM : 2404853
# Kelas : RPL 1 C
# counting sort
import timeit
start = timeit.default_timer()
def counting_sort(arr):
    maxNum = max(arr)
    count = [0] * (maxNum + 1)
    for num in arr:
        count[num] += 1
    output = []
    for i in range (len(count)):
        output.extend([i] * count[i])
    return output
unsorted = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]
sorted = counting_sort(unsorted)
print(sorted)
stop = timeit.default_timer()
print('Time: ', stop - start, " seconds")