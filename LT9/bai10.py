class SinhVien:
    def __init__(self,ten,  diem):
        self.ten = ten
        self.diem = diem
    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.ten == other.ten and self.diem == other.diem
        return False

    def __str__(self):
        return f"{self.ten} {self.diem} điểm"

sv1 = SinhVien('Trà',10)
sv2 = SinhVien('Linh', 9.8)

print(f'So sánh {sv1} = {sv2}: {sv1==sv2}')
