import numpy as np
import pandas as pd

#NumPy Dizisini Normalleştir
#NumPy dizisinin oluşturulması
data = np.array([[13, 16, 19, 22, 23, 38, 47, 56, 58, 63, 65, 70, 71]])

#dizideki tüm değerlerin normalize edilmesi
data_norm = (data - data.min())/ (data.max() - data.min())

#normalize edilen değerlerin yazdırılması
print("ilk format")
print(data_norm)

#Pandas DataFrame'deki Tüm Değişkenlerin Normalleştirilmesi
#DataFrame oluşturulması
df = pd.DataFrame({'points': [25, 12, 15, 14, 19, 23, 25, 29],
                   'assists': [5, 7, 7, 9, 12, 9, 9, 4],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12]})

#tüm sütunlardaki değerlerin normalize edilmesi
df_norm = (df-df.min())/ (df.max() - df.min())

#normalize edilen DataFrame'ler
print("ikinci format")
print(df_norm)


#Pandas DataFrame'de Belirli Değişkenleri Normalleştiri
#DataFrame oluşturulması
df = pd.DataFrame({'points': [25, 12, 15, 14, 19, 23, 25, 29],
                   'assists': [5, 7, 7, 9, 12, 9, 9, 4],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12]})

#normalleştirmek için sütunların tanımlanması
x = df.iloc[:,0:2]

#yalnızca ilk iki sütundaki değerlerin normalleştirilmesi
df.iloc[:,0:2] = (x-x.min())/ (x.max() - x.min())

#Yalnızca ilk iki sütundaki değerlerin normalize edildi
#normalize edilen DataFrame'lerin yazdırılması
print("üçüncü format")
print(df)

#Sıfırdan standart sapmayı hesaplama
values = [4,5,6,6,6,7,8,12,13,13,14,18]
# Standart sapmanın hesaplanması
mean = sum(values) / len(values)
differences = [(value - mean)**2 for value in values]
sum_of_differences = sum(differences)
standard_deviation = (sum_of_differences / (len(values) - 1)) ** 0.5

print("standart sapma")
print(standard_deviation)
# Returns: 1.3443074553223537

# z-score'un hesaplanması
zscores = [(value - mean) / standard_deviation for value in values]

print(zscores)

#  örnek Pandas Dataframe veri yüklenmesi

df = pd.DataFrame.from_dict({
    'Name': ['Nik', 'Kate', 'Joe', 'Mitch', 'Alana'],
    'Age': [32, 30, 67, 34, 20],
    'Income': [80000, 90000, 45000, 23000, 12000],
    'Education' : [5, 7, 3, 4, 4]
})

print(df.head())