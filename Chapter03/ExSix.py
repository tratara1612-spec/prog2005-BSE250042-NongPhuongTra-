def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    return count

n = [43, 423, 23, 76, 94, 543, 124]
print(f'Danh sách ban đầu:{n}')
a_count = bubble_sort(n)
print('Danh sách sau khi sắp xếp', n)
print(f'Số lần hoán đổi thực hiện:{a_count}')
