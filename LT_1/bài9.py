class Student:
    def __init__(s, ten, diem):
        s.ten = ten
        s.diem = diem

    def __str__(s):
        return f"Tên: {s.ten}, Điểm: {s.diem}"

    def display(s):
        print(f"Sinh viên {s.ten} có điểm là {s.diem}")



s1 = Student('Nguyễn Văn A', 10)
s2 = Student('Nguyễn Thị B', 9.0)

s1.display()
s2.display()
