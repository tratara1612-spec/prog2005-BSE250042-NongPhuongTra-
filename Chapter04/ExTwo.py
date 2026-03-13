def diem_tb(DS_SV):
    if not DS_SV:
        return 0
    diem = DS_SV.values()
    TB = sum(diem)/len(diem)
    return TB

SV = {'Linh': 9.0, 'Nhi': 7.5, 'Trà': 9.0}
print (f'Điểm trung bình: {diem_tb(SV)}')
