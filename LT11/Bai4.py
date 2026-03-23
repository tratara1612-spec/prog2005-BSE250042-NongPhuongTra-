ds = [23, 1, 43, 65, 78, 34, 23]
print(f'Danh sách ban đầu: {ds}')
ds[3] = 59
k = int(input('Nhập giá trị bạn muốn tìm: '))
xh = ds.count(k)
print(f'Số lần {k} xuất hiện: {xh}')
def nt(n):
    if n < 2: return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        if n % i == 0:
            return False
    return True
tong_nt = sum([x for x in ds if nt(x)])
print(f'Thêm phần tử vào danh sách: {ds}')
print(f"Tổng các số nguyên tố trong danh sách: {tong_nt}")
ds.sort()
print(f"Danh sách sau khi sắp xếp: {ds}")
ds.clear()
print(f"Danh sách sau khi xóa sạch: {ds}")
