#örnek 1: kullanıcıdan alınan integer sayının kaç basamaklı olduğunu bize geri döndüren recursive fonksiyonu yazınız.

#x=int(input("Sayı Giriniz:")) #kullanıcıdan sayı alınır
def basamakSayisi(x):
    if x<10: #10 dan küçükse 1 basamaklıdır.
        return 1
    else: #10 dan büyükse
        return 1+basamakSayisi(x//10) #x//10 ile x'in 10'a bölümünden kalanı alıyoruz.
#print(basamakSayisi(x))

#örnek 2: faktöriyel hesaplayan fonksiyonu recursive olarak yazınız.

def faktoriyel(x):
    if x==1:
        return 1
    else:
        return x*faktoriyel(x-1)
#print(x,"sayısının faktöriyeli:",faktoriyel(x))


#örnek 3: verilen listedeki elemanların toplamını bulan recursive fonksiyonu yazınız.

x=[1,2,3,4,5,6,7,8,9,10]
def toplam(x):
    if len(x)==1: #liste 1 elemanlı ise
        return x[0] #liste sonuna gelince döngüden çıkılır.
    else: #liste 1 elemanlı değilse
        print("yeni liste",x[1:])
        return x[0]+toplam(x[1:]) #x[1:] ile listedeki elemanların 1. elemanını alıyoruz.
#print(toplam(x))


#örnek 4: üs alma fonksiyonu recursive olarak yazınız.
x=int(input("Sayı Giriniz:"))
y=int(input("Üs Giriniz:"))
def ust(x,y):
    if y==1:
        return x
    else:
        print("yeni x:",x,"yeni y:",y)
        print(ust(x,y-1)*x)
        return x*ust(x,y-1)
#print(x,"sayısının",y,"üsü:",ust(x,y))