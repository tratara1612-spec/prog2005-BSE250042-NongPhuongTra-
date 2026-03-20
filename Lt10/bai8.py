def bubblue_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f'Đổi chỗ: {arr}')

        if not swapped:
            break
    return arr
ds = []
for i in range(5):
    ds.append(input(f'Nhập chuỗi {i+1}: '))

print("\n---Quá trình sắp xếp---")
ket_qua = bubblue_sort(ds)

print("\nKết quả cuối cùng (Giảm dần):", ket_qua)
