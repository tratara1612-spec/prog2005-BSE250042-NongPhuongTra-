def tuple(n):
    tong = sum(n)
    lon_nhat = max(n)
    be_nhat = min(n)
    return tong, lon_nhat, be_nhat
n_tuple = (12, 342, 5, 235, 64, 32)
tong, lon, be = tuple(n_tuple)
print(f'Tổng: {tong}, Lớn nhất: {lon}, Bé nhất: {be}')
