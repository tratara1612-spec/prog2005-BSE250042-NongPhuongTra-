import os
path = 'd:\\music\\muabui.mp3'

def lay_ten_va_duoi(path):
    return os.path.basename(path)
def lay_ten_rieng(path):
    ten_day_du = os.path.basename(path)
    return os.path.splitext(ten_day_du)[0]

print(f"Tên tệp đầy đủ: {lay_ten_va_duoi(path)}")
print(f"Chỉ lấy tên bài hát: {lay_ten_rieng(path)}")
