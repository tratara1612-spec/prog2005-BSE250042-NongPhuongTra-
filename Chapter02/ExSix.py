def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)

so = int(input("Nhập một số để tính giai thừa: "))
if so < 0:
    print("Không tính được giai thừa cho số âm.")
else:
    print(f"{so}! = {tinh_giai_thua(so)}")
