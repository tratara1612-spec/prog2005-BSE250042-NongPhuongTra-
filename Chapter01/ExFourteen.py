import math
n = float(input("Nhập một số: "))

if n >= 0:
    print(f"Căn bậc hai của {n} là: {math.sqrt(n)}")
else:
    print("Lỗi: Không thể tính căn bậc hai của số âm.")
