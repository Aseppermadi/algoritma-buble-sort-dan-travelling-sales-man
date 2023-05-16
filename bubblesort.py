def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


# Contoh penggunaan program
arr = [29, 10, 14, 37, 13]
bubble_sort(arr)
print("Hasil pengurutan:")
for num in arr:
    print(num, end=" ")
