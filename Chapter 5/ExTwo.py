import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y1 = x**2
y2 = x**3

plt.figure(figsize=(8, 5))

plt.plot(x, y1, color='blue', label='$y = x^2$')
plt.plot(x, y2, color='red', label='$y = x^3$')

plt.title("Đồ thị hàm số $y=x^2$ và $y=x^3$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend() # Hiển thị chú thích
plt.grid(True, linestyle='--')

plt.show()
