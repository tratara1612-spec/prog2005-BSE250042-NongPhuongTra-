class Student:
    def __init__(s, ten, diem):
        s.ten = ten
        s.diem = diem
    def __str__(s):
        return f"Tên: {s.ten}, Điểm: {s.diem}"

s1 = Student ('Nguễn Văn A', 10)
s2 = Student ('Nguyễn Thị B', 9.0)
print(f'Sinh viên 1:{s1}'
      f'\nSinh Viên 2:{s2}')
