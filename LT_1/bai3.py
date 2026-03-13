n = int(input('Nhập một số trong khoảng từ 1 đến 9: '))
if 1<=n<=9:
    print(f'---Bảng cửu chương{n}---')
    for i in range(1, 10):
            print(f'{n}*{i} = {i*n}')
