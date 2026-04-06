def xep_loai_hoc_tap():
    try:
        a = float(input("Nhập điểm môn a: "))
        b = float(input("Nhập điểm môn b: "))
        c = float(input("Nhập điểm môn c: "))

        dtb = (a + b + c) / 3
        print(f"\nĐiểm trung bình của bạn là: {dtb:.2f}")


        if dtb >= 8.0:
            print("Xếp loại: Giỏi")
        elif dtb >= 6.5:
            print("Xếp loại: Khá")
        elif dtb >= 5.0:
            print("Xếp loại: Trung bình")
        else:
            print("Xếp loại: Yếu")

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số thực cho điểm các môn!")

xep_loai_hoc_tap()
