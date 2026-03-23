import csv

print("--- Nhập thông tin Nhân viên ---")
ten = input("Nhập tên nhân viên: ")
tuoi = input("Nhập tuổi: ")
id_nv = input("Nhập ID nhân viên: ")

data = [id_nv, ten, tuoi]
header = ["ID", "Tên", "Tuổi"]

try:
    with open("nhanvien.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(f"ID: {id_nv}\n")
        txt_file.write(f"Tên: {ten}\n")
        txt_file.write(f"Tuổi: {tuoi}\n")
    print("\n✅ Đã lưu vào file nhanvien.txt")
    with open("nhanvien.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerow(data)
    print("✅ Đã lưu vào file nhanvien.csv")
    print("\n--- Nội dung file vừa tạo ---")
    print("Nội dung TXT:")
    with open("nhanvien.txt", "r", encoding="utf-8") as f:
        print(f.read())

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
