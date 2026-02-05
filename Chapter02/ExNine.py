n = input("Nhập vào một số nguyên dương 5 chữ số: ")

if len(n) == 5 and n.isdigit():
    max_digit = max(n)
    print(f"Chữ số lớn nhất trong {n} là: {max_digit}")
else:
    print("Vui lòng nhập chính xác 5 chữ số.")
