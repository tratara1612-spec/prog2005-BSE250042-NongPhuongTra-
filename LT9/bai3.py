def toi_uu_hoa(s):
    cac_tu = s.split()
    ra = " ".join([tu.capitalize() for tu in cac_tu])
    return ra
vao = 'nGUYễn  KháNh    SƠN  '
print(f'Dữ liệu tên người dùng ban đầu: {vao}')
print(f'Chuẩn hóa tên người dùng: {toi_uu_hoa(vao)}')
