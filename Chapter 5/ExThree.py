import matplotlib.pyplot as plt

products = ['A', 'B', 'C', 'D', 'E']
sales = [30, 25, 15, 20, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

plt.figure(figsize=(7, 7))

plt.pie(sales, labels=products, autopct='%1.0f%%', startangle=140, colors=colors)

plt.title("Phần trăm doanh số của 5 sản phẩm")
plt.show()
