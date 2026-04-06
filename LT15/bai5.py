def count_vowels(s):
    na = 'ueoaiUEOAI'
    tong=0
    for kt in s:
        if kt in na:
            tong+=1
    return tong
vao='Ối dồi ôi'
kq = count_vowels(vao)
print('Số ký tự',kq)
