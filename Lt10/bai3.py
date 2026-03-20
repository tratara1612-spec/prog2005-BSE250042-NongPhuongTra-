def dq_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * dq_giai_thua(n-1)
so = int(input('Nhập một só để tính giai thừa: '))
if so < 0:
    print('Không tính được giai thừa khi số âm!')
else:
    print(f'{so}! = {dq_giai_thua(so)}')
