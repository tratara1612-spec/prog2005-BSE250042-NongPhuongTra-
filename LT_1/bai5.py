import random
m = int(input('Nhập số hàng M: '))
n = int(input('Nhập số cột N: '))

ma_tran = [[random.randint(1,100) for i in range(n)] for i in range(m)]
print ('\n---Ma trận vừa tạo---')
for h in ma_tran:
    print(h)

hang_bat_ky = int(input(f'\nBạn muốn hiển thị hàng (1-{m}): '))
if 1 <= hang_bat_ky <= m:
    print(f'Hàng {hang_bat_ky}: {ma_tran[hang_bat_ky-1]}')
else:
    print('Số hàng không hợp lệ!')

cot_bat_ky = int(input(f'\nBạn muốn hiển thị hàng (1-{n}): '))
if 1 <= cot_bat_ky <= n:
    c = [hang[cot_bat_ky-1] for hang in ma_tran]
    print(f'Cột {cot_bat_ky}: {c}')
else:
    print('Số cột không hợp lệ!')

lon_nhat = max([lon for cot in ma_tran for lon in cot])
print(f'\n---Giá trị lớn nhất trong ma trận là: {lon_nhat}')
