def kt_chuoi():
    try:
        chuoi = input('Nhập chuỗi của bạn: ')
        if not chuoi:
            raise ValueError("Lỗi: Chuỗi nhập vào không được để trống!")
        kq = len(chuoi)
        print(f'Chuỗi của bạn dài: {kq}')
    except ValueError as e:
        print(e)
kt_chuoi()
