def selection_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, n-i):
            if arr[j] > arr[i-1]:
                arr[j], arr[i-1] = arr[i-1], arr[j]
        arr[i], arr[n-1] = arr[n-1], arr[i]
    return arr
nhap = input('Nhập dãy của bạn: ')
s = [int(x) for x in nhap.split()]
r = selection_sort(s)
r.reverse()
print('---Danh sách sử dụng thuật toán sắp xếp chọn để sắp xếp mảng theo thứ tự giảm dần---')
print(f'Mảng theo thứ tự sắp xếp: {r}')
