# from functools import reduce

# a = "abcdefgh"
# b = reduce(lambda a, b: a.upper() + b.lower(), list(a.strip(' ')))

# print(list(a.strip(' ')))
# print(b)

print()


# lambda
def carp(a, b):
    return a * b


carp1 = lambda a, b: a * b


# print(carp(5, 6))
# print(carp1(5, 6))


# map
def myfunc(a):
    return len(a)


x = map(myfunc, ('python', 'programlama', 'dili'))


# print(list(x))


def f(a):
    return a * a


x = map(f, [1, 2, 3, 4])
# print(list(x))

# map-lambda
f = lambda a: a * a

x = map(f, [1, 2, 3, 4])

# print(list(x))

# kodu kısaltabiliriz

x = map(lambda a: a * a, [1, 2, 3, 4])

# print(list(x))

# map örnek
f = lambda a, b: a + " " + b

x = map(f, ["python", "dili", "fonksiyonel"],
        ["programlama", "ile", "programlama"])

# print(' '.join(list(x)))

# print(list(x))


# filter

x = list(range(10))

f = lambda a: a % 2 == 0

s = filter(f, x)
# print(list(s))


# reduce


from functools import reduce

f = lambda a1, a2: a1 + a2

s = reduce(f, [1, 2, 3, 4])

# print(s)


# faktöriyel örneği

from functools import reduce

f = lambda a1, a2: a1 * a2
s = reduce(f, range(1, 5))
# print(s)

import os

print(os.getcwd())


def fib2(n):
    if n <= 1:
        return 1
    else:
        return fib2(n - 1) + fib2(n - 2)


print(fib2(5))

fs = dict()


def fib(n):
    if n <= 1:
        fs[str(n)] = 1
        return 1
    elif str(n - 1) in fs:
        fs[str(n)] = fs[str(n - 1)] + fs[str(n - 2)]
        return fs[str(n)]
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))

ilker = ["a", 1, 2, 3, "b", "c", 4, 5, 6]
print(type(ilker))
print(str(ilker))
ahmet = [i for i in ilker if str(i).isdigit()]

print(ahmet)

##########################
# bütünlemeye hazırlık
##########################

print("########################BÜTÜNLEME###########################")

# soru-1

x = list(range(1, 10, 2))
y = sum(x[1::2])

# verilen programa göre y değeri kaç olmalıdır?

print(y)

print(x)
print(x[1::2])

# soru-2
x = [
    {"programlama": 43, "veritabani": 12},
    {"programlama": 23, "veritabani": 5},
    {"programlama": 12, "veritabani": 13},
]

# z = 30

# yukarıdaki kod parçası çalıştırıldığında, z = 30 değerini almaktadır
# Burada, ders adı ve dersi alan öğrenci sayılarını ifade eden x veri yapısından
# veritabanı dersini alan öğrenci sayıları liste üretici ile tek satırda
# liste olarak elde edilmiş ve sum gömülü fonksiyonu ile bu listenin toplamı bulunmuştur.
# Verilenlere göre, tek satırlık liste üreticisinin tamamını yazınız.

z = sum(x[i]["veritabani"] for i in range(len(x)))

zz = sum([c[1] for c in [[v for k, v in s.items()] for s in x]])

print(z)

print(zz)

# soru-3

from functools import reduce


def tester():
    def reducer(b):
        return reduce(lambda i, j: i + j, b)

    return reducer


x = tester()

print(x(range(5)))

# verilen high-order fonksiyonunun ekran çıktısı ne olur.


# soru-4

x = ["a", 1, "b", "c", 2, 3]

y = sum([k * 2 for k in [i ** 2 for i in x if str(i).isdigit()]])

# print(list(i**2 for i in x if str(i).isdigit()))

# print(list(k*2 for k in [i**2 for i in x if str(i).isdigit()]))

print(y)

# verilen programa göre y değeri kaç olmalıdır?


# soru-5

x = ["a", "b", "c"]
y = [1, 2, 3]
z = zip(x, y)

# verilen programa göre
# {'a': 1, 'b': 2, 'c': 3}
# çıktısını görebilmek için son satıra ne gelmelidir?

print(dict(z))

# soru-6

print("{1} {0} {2} {3} {4}".format(5, 4, 1, 2, 3))

# verilen programa çıktısı ne olur?
# 4 5 1 2 3

# 0: 4
# 1: 5
# 2: 1
# 3: 2
# 4: 3 gelmiş olur


# soru-7

x = range(1, 10)[5]  # 5. elemanı alır {1,2,3,4,5,6,7,8,9}
print(x)

x = x * 2 if x % 2 == 0 else x / 2  # x%2==0 ise x*2, değilse x/2

print(x)

# soru-8

import random

numbers = [random.random() for i in range(50)]
print(numbers)

enk, enb, ort = min(numbers), max(numbers), sum(numbers) / len(numbers)

print(enk, ort, enb)

# verilen program ile üretici kullanılarak 0-1 aralığında 50 adet sayı üretilmiş
# ve bu listenin içinden en küçük (enk), en büyük (enb) ve ortalama (ort)
# yazdıran toplam 4 satırlık programı yazınız.


# soru-10

def test(a):
    a*=2
    yield a

x = test(5)
# next(x)
# print(next(x))


# soru-11
from functools import reduce

dosya = [1,"ali","veli",2,3,"ayşe",4]

print("soru-11:")

# yukarıdaki gibi bir dosya veri yapısında hem sayı hem string değişkenler vardır
# bu değişken içinden sadece sayısal değerleri süzüp (filter)
# bunları tembel değerlendirme ile toplayan (reduce) program ve çıktısı verilmiştir.
# buna göre print ifadesinin tamamını yazınız.

print(reduce(lambda i, j: i + j, [i for i in dosya if type(i) == int]))

print("filter ile çözüm: ",list(filter(lambda i: type(i) == int, dosya)))

# soru-12

sifreler = ["a123A", "Banana.123", "23dd153", "Apricot", "Or1ange"]

x=filter(lambda s:all([any([x.isdigit() for x in s]), any([x.isupper() for x in s]), len(s)>6]) ,sifreler)
print(list(x))

# verilen program, sifreler listesi içinde en az bir büyük harf,
# en az bir küçük harf içeren ve 6 karakterden uzun olan şifreleri filtrelemektedir.
# program filter içinde tanımlı bir lambda fonksiyonu ve liste üreticilerden faydalanarak
# tek satırda yazılmıştır. buna göre bu satırın tamamını yazınız.


# soru-13

from functools import reduce

f = lambda a1, a2: a1 * a2

s = reduce(f, range(5))

print(s)


# soru-14
x =  "python programlama dili"

x = x[-6:-18:-5] # -6. karakterden -18. karakterine kadar -5 aralığında karakterleri alır
# -6: a
# -11: a
# -16: p

print(x)


# soru-15

f= lambda n: 1 if n==1 else n*f(n-1)

print(f(5))


###################################
# Vize Öncesi Çalışma Soruları
##################################

x=["MerhaBA", "PYTHON", "pROGRAMLAMA", "Dili"]
y=[i.title() for i in x]
print(' '.join(y))



###################################
# 2022 vize sınavı çıkmış sorular ve çözümleri
##################################

# soru-1
from functools import reduce

a=["python","programlama","dili","ile","fonksiyonel","programlama"]
b= len(list(filter(lambda a:len(a)>3, a))) # a listesindeki elemanların uzunluğu 3'den büyük olanları alır
c=reduce(lambda a,b:a*b, range(1,b+1))

print(c)


# soru-2

from functools import reduce

a="abcdefghijklmnopqrstuvwxyz"
b = reduce(lambda a,b:a.upper()+b.lower(), list(a.strip(' ')))
print(b)

###
# soru-2 incelme
print(list(a.strip(' ')))

# soru-3

items = ["a","b","a","c","d","c","b","a"]
# listesindeki her bir elemanın kaç defa geçtiği
# ['a': 3, 'b': 2, 'c': 2, 'd': 1]
# şeklinde sözlük yapısı oluşturan python teh satırlık kodu
# fonksiyonel programlama kullanalar yazınız.

cevap = {i:items.count(i) for i in items}
print(cevap)


# soru-4

# geliştirilecek bir otomasyonda doğrudan NO-SQL bir veritabanı foreign_key
# alanında kullanılmak üzere harf ve rakamlardan oluşan unique stringler üretilecektir.
# aşağıdaki gibi x listesinde bunların olduğunu varsayarak, bu listenin sadece unique (tekil)
#olanları alan python tek satırlık kodu yazınız

x = ["a1","b1","a1","1a","abc123","1a2b","b1"]

y=list(set(x))
print(y)


# soru-5
x="Python" #stringini alıp
# ['P', 'Py', 'Pyt', 'Pyth', 'Pytho', 'Python'] listesini üreten
# tek satırlık kodu yazınız.

y = [x[0:i+1] for i in range(0,len(x))]

print(y)


###################################
# 2022 final sınavı soruları ve çözümleri
##################################

print("###################################")
print("final sınavı çözümleri")
print("###################################")

#soru-1
#öncelikle string cümleyi alıp split ile değerlerine ayırıyordu
#daha sonra bu değerleri tek tek kontrol edip
#uzunluğu 3ten küçük olanları direkt yazdırıyordu
#büyük olanları da tersine çeviriyordu

from functools import reduce

x = map( lambda a : a [::-1] if len(a) > 3 else a,  "Why i do love Python?".split(" "))
print(list(x))


# soru-2

print(reduce(lambda a,b:a**b, range(-1,6,2)))


# soru-3

urls = ['www.firat.edu.tr', 'www.kartoyunu.com', 'www.bahisvar.com', 'www.google.com', "www.aaapython.org"]
bans = 'kart bahis aaa'

#bans değerindeki harfleri içermeyen urls listesini oluşturunuz

c = filter(lambda a: not any([i in a for i in bans]), urls)
print(list(c))

a = list(filter(lambda a: a not in bans, urls))
b = list(filter(lambda a: any([1 if ban in a else 0 for ban in bans.split(' ')]), urls))
#print(a)

#print(b)

# soru-4
satislar = [
    {"tur": "su", "adet": 2},
    {"tur": "domates", "adet": 3},
    {"tur": "poşet", "adet": 1},
    {"tur": "su", "adet": 4},
]

# "tur" değeri su olan ürünlerin adet toplamı kaçtır?
toplam = sum([item["adet"] for item in satislar if item["tur"] == "su"])

print(toplam)

######################################
# bütünleme çözümleri
######################################

# "Neden Python Programlamayı Seviyorum?" how to convert to "Seviyorum? Programlamayı Python nedeN"

soru1= (' '.join("Neden Python Programlamayı Seviyorum?".split(' ')[::-1]))

print(soru1)

# 1'den n'e kadar olan sayıların s değeri kadar artarak çarpımlarını bulunuz

n=5
s=2
soru_2 = reduce(lambda a,b:a*b, range(1,n,s))
print(soru_2)

