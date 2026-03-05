def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
nhap = input('Nhập danh sách số thực của bạn cách nhau bằng dấu cách: ')
try:
    n = [float(x) for x in nhap.split()]
    insertion_sort(n)
    print('\n---Danh sách sau khi sắp xếp---')
    print(n)
except ValueError:
    print('Hãy nhập số hợp lệ!')

