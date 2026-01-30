for i in range(1, 4):
    print(f"\n--- Nhập thông tin sinh viên {i} ---")
    ten = input("Tên sinh viên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: ")) 
    dtb = (toan + ly + hoa) / 3
    print(f"Sinh viên: {ten} | Điểm trung bình: {round(dtb, 2)}")
