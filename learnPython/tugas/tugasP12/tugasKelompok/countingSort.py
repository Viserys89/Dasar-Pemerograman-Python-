# counting sort
def counting_sort(arr):
    maxNum = max(arr)
    count = [0] * (maxNum + 1)
    print(count)
    for num in arr:
        count[num] += 1
    print(count)
    output = []
    for i in range (len(count)):
        output.extend([i] * count[i])
    return output
unsorted = [4, 1,1,1,1,1,2,8,6,7,10,1,3,5,9]
sorted = counting_sort(unsorted)
print(sorted)