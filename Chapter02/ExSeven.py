a = int(input("Nhập số nguyên dương thứ nhất: "))
b = int(input("Nhập số nguyên dương thứ hai: "))

while b != 0:
    a, b = b, a % b

print(f"Ước số chung lớn nhất là: {a}")
