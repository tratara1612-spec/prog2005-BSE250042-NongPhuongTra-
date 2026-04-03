class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


book_sample = Book("Python Cơ Bản", 150000)


print(f"Giá của đối tượng book_sample là: {book_sample.price}")


list_books = [
    Book("Book 1", 30000),
    Book("Book 2", 50000),
    Book("Book 3", 100000)
]

tong_tien = 900000
file_name = "books_data.txt"

try:
    with open(file_name, "w", encoding="utf-8") as f:
        for b in list_books:
            line = f"{b.name};{b.price}\n"
            f.write(line)

        # Ghi dòng tổng cộng
        f.write(f"Tong;{tong_tien}")

    print(f"---")
    print(f"Đã tạo file '{file_name}' thành công với format yêu cầu.")

except Exception as e:
    print(f"Lỗi khi xử lý file: {e}")
