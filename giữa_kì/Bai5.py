import os:
Flie_name = 'Giữa kỳ.txt'

def bai_1():
    a = int(input('Nhập hệ số a: '))
    b = int(input('Nhập hệ số b: '))
    c = int(input('Nhập hệ số c: '))

    lon_nhat = max(a, b, c)
    nho_nhat = min(a, b, c)

    print(f'Số lớn nhất là:{lon_nhat}')
    print(f'Số bé nhất là: {nho_nhat}')

def bai_2():
    for x in range(17, 112):
        if x % 2 != 0:
            print(x, end=' ')


def bai_3():


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

while True:
    print('---Menu bài làm kiểm tra giữa kỳ---')
    print('1. Câu 1')
    print('2. Bai 2')
    print('3. Bai 3')
    print('4. Bai 4')
    print('5. Thoát')
    chon = input('Nhập lựa chọn của bạn: ')
    if chon == '1':
        bai_1()
    elif chon == '2':
        bai_2()
    elif chon == '3':
        bai_3()
    elif chon == '4':
        selection_sort()
    elif chon == '5':
        break
    else:
        print('Vui lòng chọn lại')
