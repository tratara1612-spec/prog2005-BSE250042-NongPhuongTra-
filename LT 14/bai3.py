
nums = [int(x) for x in input("Dãy số: ").split()]

le = [x for x in nums if x % 2 != 0]
print(f"Lẻ: {le}, Số lượng: {len(le)}")

so_nguyen_to = []
for x in nums:
    if x < 2:
        continue
    is_prime = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        so_nguyen_to.append(x)

print(f"Các số nguyên tố: {so_nguyen_to}")
