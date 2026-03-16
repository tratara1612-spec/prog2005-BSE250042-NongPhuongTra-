n = input('Nhập chữ số của bạn: ')
tong = sum(int(so) for so in n if so.isdigit())
print(f'Tổng các chữ số của {n} là: {tong}')
