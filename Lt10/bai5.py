import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, x**2, 'b')
ax1.set(title='Đồ thị $y = x^2$', xlabel='x', ylabel='y')

ax2.plot(x, np.sqrt(x), 'r')
ax2.set(title='Đồ thị $y = \sqrt{x}$', xlabel='x', ylabel='y')

plt.tight_layout()
plt.show()
