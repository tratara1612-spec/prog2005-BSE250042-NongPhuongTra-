arr = [input(f'Nhập chuỗi {i+1} của bạn: ') for i in range(5) ]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and len(key) > len(arr[j]):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print(f"Bước {i} (Chèn '{key}'): {arr}")
nhi_phan = input('\nNhâp chuỗi cần tìm: ')
low, high = 0, len(arr) -1
pos = -1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == nhi_phan:
        pos = mid
        break
    if len(arr[pos]) > len(nhi_phan):
        low = mid + 1
    else:
        high = mid - 1
print(f'Vị trí tìm thấy: {pos}' if pos != -1 else 'Không tìm thấy')
