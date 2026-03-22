import matplotlib.pyplot as plt
import pandas as pd

data = {
    'city': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno', 
             'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim', 'Riverside'],
    'area_total_km2': [1302, 964, 466, 600, 290, 259, 210, 202, 393, 131, 211]
}

df = pd.DataFrame(data)

df_sorted = df.sort_values(by='area_total_km2', ascending=False)

top_10_cities = df_sorted.head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_10_cities['city'], top_10_cities['area_total_km2'], color='teal')

plt.xlabel('Diện tích ($km^2$)')
plt.ylabel('Thành phố')
plt.title('Top 10 thành phố lớn nhất California theo diện tích')
plt.gca().invert_yaxis() # Đảo ngược trục Y để thành phố lớn nhất nằm ở trên cùng
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()
