import matplotlib.pyplot as plt
hoc_luc = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
so_luong = [6, 10, 12, 4, 1]
plt.bar(hoc_luc, so_luong)
plt.title('Kết quả học tập của lớp')
plt.xlabel('Học lực')
plt.ylabel('Số lượng học sinh')
plt.show()
