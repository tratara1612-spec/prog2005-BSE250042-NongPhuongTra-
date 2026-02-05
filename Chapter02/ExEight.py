n = int(input("Nhập một số dương: "))
so_dao_nguoc = 0

while n > 0:
    chu_so_cuoi = n % 10
    so_dao_nguoc = so_dao_nguoc * 10 + chu_so_cuoi
    n //= 10

print(f"Số sau khi đảo ngược là: {so_dao_nguoc}")
