weight = float(input('Nhập cân nặng của bạn (kg): '))
height = float(input('Nhập chiều cao của bạn (m): '))
BMI = weight / (height * height)
print(f'Chỉ số BMI của bạn là: {round(BMI,2)}')
