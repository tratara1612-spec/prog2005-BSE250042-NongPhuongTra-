def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
so = int(input('Nhập số để tính giai thừa: '))
if so < 0:
    print('Không thể tính giai thừa số âm!')
else:
    print(f'{so}!={giai_thua(so)}')
