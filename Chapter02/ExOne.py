n = int(input("Nhập một khoảng từ 1 đến 9: "))
if 1<=n<=9:
    print(f"Bảng cửu chương {n}: ")
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")
else:
    print("Vui lòng nhập đúng số trong khoảng 1-9.")
