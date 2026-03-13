import math

def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n = input('Nhập chuỗi của bạn cách nhau bằng dấu cách: ')
danh_sach_so = [int(x) for x in n.split(' ')]
chan = am = n_to = tong = 0

print("---Các số trong chuỗi---")
for x in danh_sach_so:
    print(x, end=' ')
    if x % 2 == 0: chan += 1
    if x < 0: am += 1
    if la_so_nguyen_to(x): n_to += 1
    tong += x

print(f"\nSố chẵn: {chan}")
print(f"Số âm: {am}")
print(f"Số nguyên tố: {n_to}")
print(f"Trung bình cộng: {tong / len(danh_sach_so)}")
