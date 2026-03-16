n = input('Nhập chuỗi của bạn: ')
hoa = thuong = chu_so = dac_biet = trang = nguyen_am = phu_am = 0
na = 'ueoaiUEOAI'
for s in n:
    if s.isupper():
        hoa += 1
    if s.islower():
        thuong += 1
    if s.isdigit():
        chu_so += 1
    if s.isspace():
        trang += 1
    if not s.isalnum() and not s.isspace():
        dac_biet += 1
    if s.isalpha():
        if s in na:
            nguyen_am += 1
        else:
            phu_am += 1
print('---Các dữ liệu trong chuỗi có số lượng---')
print(f"- In hoa: {hoa}\n- In thường: {thuong}\n- Chữ số: {chu_so}")
print(f"- Khoảng trắng: {trang}\n- Đặc biệt: {dac_biet}")
print(f"- Nguyên âm: {nguyen_am}\n- Phụ âm: {phu_am}")
