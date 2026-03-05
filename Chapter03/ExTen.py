data = [int(x) for x in input("Nhập danh sách số: ").split()]

even_nums = [x for x in data if x % 2 == 0]
print(f"Các số chẵn: {even_nums}, Tổng: {sum(even_nums)}")
