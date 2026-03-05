def linear_search(arr, taret):
    for i in range(len(arr)):
        if arr[i] == taret:
            return i
    return -1
s = input('Nhập danh sách của bạn cách nhau bằng dấu cách: ')
arr = [int(x) for x in s.split()]
target = int(input('Nhập số cần tim: '))

result = linear_search(arr, target)
if result != -1:
    print(f'Số {target} được tìm thấy tại chỉ số: {result}')
else:
    print(f'Số {target} không tồn tại trong danh sách.')
