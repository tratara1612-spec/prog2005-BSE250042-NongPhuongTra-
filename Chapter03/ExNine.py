data = [int(x) for x in input("Nhập danh sách số: ").split()]

odd_nums = [x for x in data if x % 2 != 0]
print(f"Các số lẻ: {odd_nums}")
