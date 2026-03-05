def find_max_min(arr):
    if not arr: return None, None
    return max(arr), min(arr)

nums = [float(x) for x in input('Nhập mảng: ').split()]
mx, mn = find_max_min(nums)
print(f'Giá trị lớn nhất: {mx}, Nhỏ nhất: {mn}')
