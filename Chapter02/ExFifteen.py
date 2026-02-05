n = int(input("Nhập một số nguyên dương: "))
so_ban_dau = n
tong = 0

while n > 0:
    chu_so = n % 10 
    tong += chu_so   
    n //= 10         
  
print(f"Tổng các chữ số của {so_ban_dau} là: {tong}")
