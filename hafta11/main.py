# #negatif argüman aldığında ValueErrpr yayonlayan bir faktöriyel fonksiyonu yazalım
# import os
# from logging import exception
# def factorial(n):
#     if n == 0:
#         return 1
#     # elif n<0:
#     #     return "Negative number"
#     else:
#         return n * factorial(n-1)
#
# try:
#     print(factorial(-5))
# except:
#     print("NegativeError!!!")
import os

# print(os.getcwd())
# print(os.listdir())
# for i in os.walk(os.path.dirname("C:/Users/eymen/Desktop")):
#     print(i)

#örnek 1
# kullanıcıdan beş tane isim alıp name.txt dosyasına yazalım
with open("name.txt", "w") as f:
    for i in range(5):
        name = input("Enter your name: ")
        f.write(name + "\n")
