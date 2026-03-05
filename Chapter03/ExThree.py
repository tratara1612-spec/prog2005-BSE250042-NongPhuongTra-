mau = ['Red', 'Green', 'Pink', 'Yellow', 'Blue']
print(f'Danh sách ban đầu:{mau}')
try:
    mau.remove('Green')
    print(f'Danh sách sau khi xóa màu Green: {mau}')

except ValueError:
    print('Không tồn tại Green')
print(f'Danh sách hiện tại:{mau}')
