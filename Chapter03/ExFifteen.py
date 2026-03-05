text = input('Nhập chuỗi: ')
ex1 = text[::-1]
ex2 = ""
for char in text:
    ex2 = char + ex2

print(f"Cách 1 (Slicing): {ex1}")
print(f"Cách 2 (Looping): {ex2}")
