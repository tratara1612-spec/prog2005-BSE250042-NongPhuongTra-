mau = {'xanh', 'đỏ', 'tím', 'vàng', 'cam', 'hồng'}
tim = input('Hãy thử đoán một một có thể xuất hiện trong dictionary: ')
if tim in mau:
    print(f'Màu {tim} có tồn tại trong dictionary >w<')
else:
    print(f'Màu {tim} không có trong dictionary T^T')
