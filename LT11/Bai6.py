tt = {}
try:
    n = int(input('Danh sách có bao nhiểu người: '))
    for i in range(n):
        print(f'\n---Người thứ {i+1}---')
        ten = input('Tên: ')
        tuoi = input('Tuổi: ')
        tt[ten] = int(tuoi)
    print(f"\nDictionary thông tin: {tt}")
    if tt:
        ds = tt.values()
        tuoi_tb = sum(ds)/len(ds)
        print(f'Tuổi trung bình của danh sách là: {tuoi_tb:.2f}')
    else:
        print("Danh sách rỗng!")

except ValueError:
    print('Lỗi: Vui lòng nhập số cho số lượng người và số tuổi!')
