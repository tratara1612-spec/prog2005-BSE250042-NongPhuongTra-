d = {
    'Loài': 'Chó',
    'Tên': 'Mèo',
    'Tuổi' : 1,
}
print(f'Từ điển: {d}')
k = input('Nhập từ khóa bạn muốn tìm: ')
if k in d:
    print(f'Từ khóa {k} có trong từ điển')
else:
    print(f'Từ khóa {k} không có trong từ điển')
