def ds():
    while True:
        print('\n'+'-'*30)
        print('DANH SÁCH CÁC BÀI TẬP ĐẠI SỐ TUYẾN TÍNH')
        print('-'*30)
        print('1. Phép khử G')
        print('2. Ma trận đảo')
        print('3. Tính định thức')
        print('0. Thoát')
        print('-'*30)

        n = input('Nhập loại bài muốn làm: ')
        if n == '1':
            print('Cho hệ phương trình tuyến tính sau với tham số m:')
            print('[[1, 1, -1]\n'
                  '[2, 3, m]\n'
                  '[1, m, 3]\n')
        elif n == '2':
            print('Tìm ma trận nghịch đảo')
            print('[1   2 -1]\n'
                  '[2   5  0]\n'
                  '[-1  0  6]\n')
        elif n == '3':
            print('B =')
            print('[1  1  1  1]\n'
                  '[1  3  3  3]\n'
                  '[1  3  6  10]\n')
            print('Tính định thức của ma trận b cấp 4 bằng cách đưa về dạng tam giác')
        elif n == '0':
            print("Đang thoát chương trình Đại số...")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    ds()
