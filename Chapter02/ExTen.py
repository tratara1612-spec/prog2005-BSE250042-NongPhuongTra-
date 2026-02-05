def tinh_tong_de_quy(n):
    if n == 1:
        return 1
    return n + tinh_tong_de_quy(n - 1)

n = int(input("Nhập n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    ket_qua = tinh_tong_de_quy(n)
    print(f"Tổng các số từ 1 đến {n} là: {ket_qua}")
