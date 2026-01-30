try:
    a = int(input("Nhập số nguyên thứ nhất: "))
    b = int(input("Nhập số nguyên thứ hai: "))
    ket_qua = a / b
    print(f"Kết quả phép chia: {ket_qua}")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho số 0.")
except ValueError:
    print("Lỗi: Vui lòng nhập đúng định dạng số nguyên.")
