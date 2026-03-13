import os
FILE_NAME = 'qlds_sanpham.txt'


def nhapSP():
    print('\n---Nhập thông tin cho từng sản phẩm---')
    ma = input('Mẫ số sản phẩm: ')
    ten = input ('Tên sản phẩm: ')
    gia = float(input('Giá sản phẩm: '))

    with open(FILE_NAME, 'a', encoding="utf-8") as f:
        f.write(f'{ma},{ten},{gia}\n')
    print('---Đã lưu sản phẩm thành công---')


def docFile():
    ds_sanpham = []
    if not os.path.exists(FILE_NAME):
        return ds_sanpham
    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        for line in f:
            data = line.strip().split(',')
        if len(data)==3:
            ds_sanpham.append({
                'ma':data[0],
                'ten':data[1],
                'gia':float(data[2])
            })
    return ds_sanpham


def HienThi(ds):
    if not ds:
        print('Danh sách trống!')
        return
    print(f"{'Mã số sản phẩm':<15}|{'Tên sản phẩm':<30}|{'Giá tiền':<20}")
    print("-"*80)
    for sp in ds:
        print(f"{sp['ma']:<15},{sp['ten']:<30},{sp['gia']:<20}")


def SapXepDsGiam():
    ds = docFile()
    ds_sorted = sorted(ds, key=lambda x: x['gia'], reverse=True)
    print('\n---Danh sách sau khi sắp xếp theo giá giảm dần---')
    HienThi(ds_sorted)

while True:
    print('\n---MENU QUẢN LÝ SẢN PHẨM---')
    print('1. Nhập sản phẩm mới ')
    print('2. Hiển thị danh sách sản phẩm ')
    print('3. Sắp xếp theo giá gảm dần')
    print('0. Thoát! ')
    chon = input('Lựa chọn của bạn là: ')

    if chon == "1":
        nhapSP()
    elif chon == "2":
        print('Danh sách sản phẩm hiện có')
        HienThi(docFile())
    elif chon == "3":
        SapXepDsGiam()
    elif chon == "0":
        break
    else:
        print('Vui lòng chọn lại!')
