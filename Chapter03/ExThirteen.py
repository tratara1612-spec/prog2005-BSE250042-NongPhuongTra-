def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

text = input('Nhập chuỗi: ')
print('Là chuỗi đối xứng' if is_palindrome(text) else 'Không đối xứng')
