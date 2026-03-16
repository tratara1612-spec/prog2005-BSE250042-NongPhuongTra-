class SinhVien:
    sl = 0
    def __init__(self, ten):
        self.ten = ten
        SinhVien.sl += 1

    @classmethod
    def so_luong(cls):
        return f'Tổng số sinh viên hiện có: {cls.sl}'

sv1 = SinhVien('Trà')
sv2 = SinhVien('Linh')
sv3 = SinhVien('Nhi')
print(SinhVien.so_luong())
