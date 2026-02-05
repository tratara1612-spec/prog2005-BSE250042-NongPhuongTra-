n = int(input("Nhập số lượng số Fibonacci cần in (n): "))
a, b = 0, 1
count = 0

if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
elif n == 1:
    print(f"Dãy Fibonacci: {a}")
else:
    print("Dãy Fibonacci:", end=" ")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()
