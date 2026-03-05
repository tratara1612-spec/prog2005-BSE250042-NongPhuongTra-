def find_first_greater_than_10(arr):
    for x in arr:
        if x > 10:
            return x
    return None

data = input('Nhập danh sách số: ')
numbers = [float(x) for x in data.split()]

result = find_first_greater_than_10(numbers)
if result is not None:
    print(f'Số đầu tiên lớn hơn 10 là: {result}')
else:
    print('Không có số nào trong danh sách lớn hơn 10.')
