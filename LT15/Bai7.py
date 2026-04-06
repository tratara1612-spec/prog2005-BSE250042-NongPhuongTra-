def tinh_trung_binh(danh_sach_sv):
    if not danh_sach_sv:
        return 0
    tong_diem = sum(danh_sach_sv.values())
    return tong_diem / len(danh_sach_sv)

sinh_vien = {
    "An": 8.5,
    "Linh": 7.0,
    "Nhi": 9.0
}

dtb = tinh_trung_binh(sinh_vien)
print(f"Điểm trung bình của {len(sinh_vien)} sinh viên là: {dtb:.2f}")
