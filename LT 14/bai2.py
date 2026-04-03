Ds = []
for i in range(5):
    t = input(f'Nhập tên người thứ {i + 1}: ')
    Ds.append(t)
print('Tên 5 người trong danh sách:', Ds)
del Ds[1]
print(Ds)
