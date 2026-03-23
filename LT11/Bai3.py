try:
    n = input('Nhập chuỗi chữ số của bạn cách nhau bằng dấu cách: ').split()
    so = [int(i) for i in n]
    chan = [x for x in so if x % 2 == 0]
    if chan:
        print(f'Số chẵn trong danh sách:{chan}')
        print(f'Tổng các số chẵn: {sum(chan)}')
    else:
        print('Không có số chẵn!')
except ValueError:
    print('Vui lòng nhập số')
