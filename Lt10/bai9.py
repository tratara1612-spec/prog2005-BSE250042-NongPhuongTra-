class Xe:
    loai = "Đường bộ"

    def __init__(self, ten, gia):
        if gia < 0: raise ValueError("Giá âm!")  
        self._ten, self._gia = ten, gia

    @property
    def ten(self):
        return self._ten

    @ten.setter
    def ten(self, v):
        if not v: raise ValueError("Tên trống!")  
        self._ten = v

    def chay(self):
        return f"{self._ten} chạy"

    @classmethod
    def doi_loai(cls, l):
        cls.loai = l

    @staticmethod
    def la_dat(g):
        return g > 1000

    def __eq__(self, o):
        return self._ten == o._ten and self._gia == o._gia

    def __str__(self):
        return f"{self._ten} - {self._gia}"


class XeMay(Xe):
    def __init__(self, ten, gia, pk):
        super().__init__(ten, gia)
        self.pk = pk

    def __str__(self): return f"{super().__str__()} - {self.pk}cc"


try:
    x1 = Xe("Vin", 500)
    x2 = Xe("Vin", 500)
    xm = XeMay("SH", 150, 150)
    print('---Bảng so sánh---\n')
    print(f"Xe: {x1}\nXe máy: {xm}")
    print(f"Bằng nhau? {x1 == x2}")
    print(f"Đắt? {Xe.la_dat(1500)}")

    Xe.doi_loai("Bay")
    print(f"Loại: {Xe.loai}")

    x1.ten = ""
except ValueError as e:
    print(f"Lỗi: {e}")
