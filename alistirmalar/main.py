#hafta 1
import math

for i in range(0,10,2):
    print(i)
#ekrana 0,2,4,6,8 yazdirir

for i in range(10,0,-2):
    print(i)
#ekrana 10,8,6,4,2 yazdirir

#hafta 2
x="p" in "Python"
print(x)
#x çıktısı False

y=5 in [3,5,7]
print(y)
#y çıktısı True


z=5 not in [3,5,7]
print(z)
#z çıktısı False

#şart ifadeleri örnek
a=200
b=33
if b>a:
    print("b daha büyük a değerinden")
elif a==b:
    print("a ve b eşittir")
else:
    print("b daha küçük a değerinden")

#else kısmı olmayan bir if örneği
a=200
b=33
if b>a:
    print("b daha büyük a değerinden")

#temel tipler (integer, string, boolean, double)
#diğer veri tipleri
#list (liste)
#tuple (demet)
#set (küme)
#dictionary (sözlük)

#listeler
liste=[1,2,"a",3,5]
print(liste)
#liste çıktısı [1, 2, 'a', 3, 5]

#dizilere benzerlerr ancak boyutları dinamiktir ve
#karışık türden veriler içerebilirler

x=list() #boş bir liste oluşturur
print(x)
#x çıktısı []

a=[] #boş bir liste oluşturur
print(a)
#x çıktısı []

# len(a) #liste içindeki eleman sayısını verir
# a.sort() #listeyi sıralar
# a.reverse() #listeyi tersine çevirir
# a.append(5) #listeye eleman ekler
# a.insert(2,3) #listeye eleman ekler ve elemanın yerine belirtilen indeksi
# a.remove(3) #listenin belirtilen elemanını kaldırır
# a.pop() #listenin son elemanını kaldırır
# a.pop(2) #listenin belirtilen indeksli elemanını kaldırır
# a.clear() #listeyi boşaltır
# a.index(3) #liste içinde belirtilen elemanın indeksini verir
# a.count(3) #liste içinde belirtilen elemanın kaç kere geçtiğini verir
# a.extend(liste) #liste içindeki elemanları başka bir listeye ekler
# a.sort() #listeyi sıralar
# a.reverse() #listeyi tersine çevirir
# a.copy() #listeyi kopyalar


#döngüler
#python dilinde döngüler daha esnektir ve listeler ile
#ileride göreceğimiz sözlük, demet, küme gibi veri yapıları
#itere edilebilir ya da diğer bir ifade ile mutable nesnelerdir.

#for döngüsü
x=[1,2,3,4,5]
t=0
for i in x:
    t+=i
print(t)
print(sum(x))
#t çıktısı 15
#sum fonksiyonu liste içindeki elemanları toplar

#range fonksiyonu
#gerek döngülerde, gerek bir sayı aralığı oluşturmak için kullanılır
#range(ilk değer, son değer, artış miktarı)
#ilk değer ve son değer arasındaki değerleri liste olarak döndürür
#artış miktarı belirtilmezse 1 olarak varsayılır

#range öncesinde bir liste değişkenine atanabileceği gibi
#doğrudan döngü nesnesi olarak kullanılabilir.
#ikinci kullanım türü Java benzeri döngü yapılarına daha çok benzemektedir.

print("range kullanımı")
x=range(10,5,-1)
for i in x:
    print(i)
#ekrana 10,9,8,7,6 yazdırır

for i in range(0,100,2):
    print(i)
#ekrana 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98 yazdırır

#for döngüsü örnek 1: asal sayı
#1 ve kendisinden başka böleni olmayacak.
#asal sayı bizim kontrol değişkenimiz.
#asal sayıyı kontrol edeceğimiz bir sayıyı belirttik.
#döngü içinde herhangi bir sayıya bölünürse
#değerini False yapıp döngüden çıkıyoruz
#Döngü sonunda değişkenin değerini tekrar kontrol ediyoruz.
asal=True
x=18
for i in range(3,x):
    if x%i==0:
        asal=False
        break

print(x," asaldır") if asal else print(x," asal değildir")
#if'ten öncesi true kısmı, else'den sonrası false kısmı ifade eder.

#for-else örnek 2: asal sayı
#asal sayı örneği: pythonic versiyon
#döngülerle birlikte else kullanabiliyoruz.
#daha az kod, kontrol değişkenine gerek yok
#else kısmı döngü sonunda çalışır.
# daha öncesinde break çalışır ise else kısmı çalışmamış olur

x=13
for i in range(3,x):
    if  x%i==0:
        print(x," asal değildir")
        break
else:
    print(x," asaldır")


#while döngüsü
#for döngüleri daha esnektir. while döngülerinde,
#döngü değişkeni ve döngü içinde bu değişkenin
#güncellenmesine ihtiyaç vardır.

x=10
t=0
i=0
while i<x:
    t+=i
    i+=1

print(t)
#t çıktısı 45


#metotlar
#def anahtar sözcüğü ile başlar, return ile sonucu geri dönderirler.

def topla(x,y):
    return x+y

print(topla(2,3))
#ekrana 5 değeri yazdırılır.


#sınıflar

#class anahtar sözcüğü ile oluşturulur, büyük harf zorunludur
# __init__ metodu yapılandırıcı metottur.
#self anahtar sözcüğü kullanımı zorunludur.
#java dilindeki this kullanımına benzer, sınıfa atıf yapar.

class Matematik:
    def __init__(self):
        self.pi=3.14

    def alan_hesapla(self,r=0):
        return self.pi*r*r

    def cevre_hesapla(self,r=0):
        return self.pi*2*r


daire=Matematik()
print("alan: ",daire.alan_hesapla(5))
print("çevre: ",daire.cevre_hesapla(4))


#HAFTA-3

#zamanı manipüle etmek için time modülünü kullanıyoruz.
import time
t1=time.time()
t1=t1+60*60

t2=time.gmtime(t1)
print(t2)

#random kütüphanesi
#varsayılan olarak bu komut ile 0 ve 1 arasında rastgele bir sayı üretir. 1 dahil değildir.
#örnek: sadece bu fonksiyonu kullanarak istenilen a-b aralığında
#tam sayı üretmeye çalışalım?

import random
print(random.random())

#5-10 aralığında sayı üretmeye çalışalım
a=5
b=10

x=a+(int)((b-a)*random.random())
print(x)

#random kütüphanesi faydalı fonksiyonlar
#shuffle, choice, sample
#choice fonksiyonu ile istenilen bir liste içinden rastgele bir eleman üretir.
#sample ise parametre sayısı olarak verilen kadar rastgele eleman seçer
#shuffle elemanları karıştırır. örneğin sınav otomasyonunda soruların herkese karışık olarak getirilmesi için kullanılabilir.


x=[1,2,3,'a','b']
print("random.choice: ",random.choice(x))
print("random.sample: ",random.sample(x,2))
random.shuffle(x)
print("random.shuffle",x)


#string işlemleri
#her string bir karakter dizisidir ve mutable nesnelerdir.
#dolayısıyla doğrudan itere edilebilirler.
#indislerin 0 dan başladığını unutmayalım.

x="Python programlama dili"
for i in x:
    print(i)

print(x[4])

#stringleri bölmek.
#stringlerden (listeler için de aynı şey geçerlidir):
# : ile belirli aralıkları parçalayabiliriz.

print(x[2:10]) #2. karakterden 10. karakter kadar
print(x[2:]) #2'den sonraki karakterleri alır.
print(x[:10]) #0'dan 10'a kadar karakterleri alır.
print(x[0::2]) #baştan sona ikişer adımla alır
print(x[::-1]) #sondan başa -1 adıma, böylece ters çevirir.

#string manipülasyonları
#lower, upper, strip, split, join
#lower, upper, strip, split, join metotları string işlemlerinde kullanılır.
#strip metotu, karakterleri siler.
#split metotu, karakterleri ayırır.
#join metotu, karakterleri birleştirir.
#lower metotu, karakterleri küçük harfe çevirir.
#upper metotu, karakterleri büyük harfe çevirir.
#replace metotu, karakterleri değiştirir.

x="python programlama dili"
print(x.strip(' '))
print(x.replace(',',' '))
print(x.upper())
print(x.lower())
print(x.split(' '))
print(':'.join(x.split(' ')))


#math modülü
#math modülündeki fonksiyonları kullanarak matematiksel işlemler yapalım.

#pow fonksiyonu, ikinci parametre olarak verilen sayıya kuvvet alır.
#sqrt fonksiyonu, karekök alır.
#ceil fonksiyonu, sayıyı yukarı yuvarlar.
#floor fonksiyonu, sayıyı aşağı yuvarlar.
#round fonksiyonu, sayıyı yuvarlar.
#abs fonksiyonu, sayıyı mutlak değerine çevirir.
#max fonksiyonu, sayıların en büyüğünü alır.
#min fonksiyonu, sayıların en küçüğünü alır.

print("math.pow(4,3) -->",math.pow(4,3))
print("math.sqrt(16) -->",math.sqrt(16))
print("math.ceil(4.5) -->",math.ceil(4.5))
print("math.floor(4.5) -->",math.floor(4.5))
print("math.pi -->",math.pi)

#locale modülü
#locale modülünün fonksiyonlarını kullanarak, sayıların formatlanmasını sağlayan bir modüldür.
#format metodu, sayıların formatlanmasını sağlar.

#kullanıcıdan girdi alma
#input metodu, kullanıcıdan girdi alır.


#HAFTA 4


#göreceğimiz veri yapıları

#Listeler (list) []
    #dinamik
#Demetler (tuple) ()
    #güncellenemezler
#Kümeler (set) {}
    #tekrar eden değerler içermezler
#Sözlükler (dict) {key:value}

#hepsi mutable nesnelerdir.


#listeler
a=[1,2,"a",3,5] #veriler karışık türden olabilir

# len(a) #eleman sayısı
# a.sort() #listeyi sıralar
# a.reverse() #listeyi ters çevirir
# a.pop() #listenin son elemanını siler
# a.append("a") #sonuna yeni eleman ekler
# a.insert(indis,"a") #yeni elemanı belirtilen indis'e ekler

#listeler enumerate
x=[1,2,3,4,5]
for i in enumerate(x):
    print(i)

for indis, eleman in enumerate(x):
    print(indis,eleman)

#listeleri birleştirmek
x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=x+y
print(z)

#çok boyutlu listeler
x=[1,2,3,4,5]   #1 boyutlu
y=[6,7,8,9,10]  #1 boyutlu
z=[x,y]         #2 boyutlu
a=[
    [1,2,3,4,5],
    [6,7,8,9,10]
]           #2 boyutlu
print(z)
print(a)

#len(z) #2 boyutlu liste için boyutu
#len(x[0]) #ilk satırdaki sütun sayısını verir.


#çok boyutlu listeler
import random
x=[]
for i in range(5):
    x.append([random.randint(1,5) for c in range(4)])

print(x)


#listeler-bölme
#x[a:b:c] #a'dan b'ye c adımda bölünür.
#a: başlangıç, b: bitiş, c: adım
x=[1,2,3,4,5]
y=x[1:3]
print(y)


#demetler
#demetler tuple'dir.
#listeler gibi kullanılırlar ama güncellenemezler.

#demetler güncelleme
#demetler doğrudan güncellenemezler
#aşağıdaki yöntemle güncelleme yapabiliriz.

#değiştirilemez demetleri nasıl değiştirebiliriz?
#demetleri listeler olarak değiştirebiliriz.
#listeye dönüştürüp değiştirdik,
#tekrar demet yapıp yeniden atama yapıtk

x=["ali","veli","hakan"]

y=list(x)

y[1]="fatma"
x=tuple(y)
print(x)

#çoklu atamalar
#hemen her veri tipinde kullanılabilir.
#metotlardan dönüş değerinin alınmasında pratik kullanım sağlar

gizliler=("ali","123")
user, sifre=gizliler
print(user,sifre)


#kümeler ??
#indeksleri yoktur, tekrar eden değer içermezler
x=(1,2,3,2,1)
print(x)
print(len(x)) #??


#sözlükler
#anahtar-değer şeklinde veri yapılarıdır.

x={"user":"ali", "şifre:":"123","login_count":5}

print(x['user']) #erişim

x['user']="ali cevher" #update
print(x['user'])

#yeni key-value ilave etme
x['tckimlik']="1234456777"

#key-value çifti silme
x.pop('tckimlik')

print(len(x))


#sözlükler üzerinde döngüler
#doğrudan itere edilebilirler
#
#
#
#
#

#sözlüklere erişim
#
#
#
#


#HAFTA 5


#üreticiler (generators)


x=[
    {"programlama":43,"veritabani":12},
    {"programlama":23,"veritabani":5},
    {"programlama":12,"veritabani":13},
   ]

z=sum([c[1] for c in [[v for k,v in s.items()] for s in x]])

print(z)

import random

numbers=[random.random() for i in range(50)]

enk,enb,ort=min(numbers),max(numbers),sum(numbers)/len(numbers)
print(enk,ort,enb)


sifreler=["a123A","Banana.123","Apricot","Or1ange"]

x=filter(lambda s:all([any([x.isdigit() for x in s]), any([x.isupper() for x in s]), len(s)>6]) ,sifreler)

print(list(x))

class Fibo:
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        self.f1, self.f2, self.i = [1,1,0]
        return self

    def __next__(self):
        while(self.i<5):
            self.f1, self.f2=[self.f2, self.f1+self.f2]
            self.i+=1
            return self.f2
        else:
            raise StopIteration

x=Fibo(5)
x=iter(x)
print(next(x))