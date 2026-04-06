def luu_vao_file():
    noi_dung = input("Nhập chuỗi ký tự bạn muốn lưu: ")
    with open("du_lieu.txt", "w", encoding="utf-8") as f:
        f.write(noi_dung)

    print("Đã lưu vào file du_lieu.txt thành công!")


luu_vao_file()
