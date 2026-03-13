import math

a = float(input('Nhập số thứ nhất: '))
b = float(input('Nhập số thứ hai: '))
if a > 0 and b > 0:
    luy_thua_1 = a**b
    chia_phan_nguyen = a//b
    chia_phan_du = a/b
    print(f'Lũy thừa: {a}**{b} = {luy_thua_1}')
    print(f'Căn bậc hai của {a}: {math.sqrt(a)}')
    print(f'Căn bậc hai của {b}: {math.sqrt(b)}')
    print(f'Chia lấy phần nguyên của {a}/{b}={chia_phan_nguyen} ')
    print(f'chia lấy phần dư của{a}/{b}={chia_phan_du} ')
    print(f'Làm tròn số: {round(chia_phan_du, 2)}')
else:
    print('Không thể tính căn bậc của số âm và không!')
    print(f'Lũy thừa: {a}**{b} = {a**b}')
}')
