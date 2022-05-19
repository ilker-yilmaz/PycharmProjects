import numpy as np
import pandas as pd

# min max normalizasyonu
# NumPy dizisi oluşturma
data = np.array([[13, 16, 19, 22, 23, 38, 47, 56, 58, 63, 65, 70, 71]])

#dizideki tüm değerlerin normalize edilmesi
data_norm = (data - data.min())/ (data.max() - data.min())

#min max ile normalize edilen değerlerin görülmesi
print(data_norm)

#z-score normalizasyonu

#DataFrame olluşturulması
df = pd.DataFrame({'yaş': [25, 12, 15, 14, 19, 23, 25, 29],
                   'uğurlu sayı': [5, 7, 7, 9, 12, 9, 9, 4],
                   'puan': [11, 8, 10, 6, 6, 5, 9, 12]})

#sütundaki tüm değerlerin normalize edilmesi
df_norm = (df-df.min())/ (df.max() - df.min())

#z-score ile normalize edilen değerlerin görülmesi
print(df_norm)

# Calculate the Standard Deviation in Python
values = [4,5,6,6,6,7,8,12,13,13,14,18]
mean = sum(values) / len(values)
differences = [(value - mean)**2 for value in values]
sum_of_differences = sum(differences)
standard_deviation = (sum_of_differences / (len(values) - 1)) ** 0.5

print("z-score:")
print(standard_deviation)

zscores = [(value - mean) / standard_deviation for value in values]
print("z-scores:")
print(zscores)
# Returns: 1.3443074553223537