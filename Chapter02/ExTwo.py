n = int(input("Nhập một số dương: "))
if n < 2:
    print(f"{n} không phải số nguyên tố.")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phảo số nguyên tố.")
