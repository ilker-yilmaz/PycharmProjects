#örnek 2:
#kendisine parametre olarak gelen sayı listesinin elemanlarını 10 ile çarparak geri döndüren fonksiyon örneğini map yardımıyla gerçekleştiriniz

def onIleCarp():
    x=map(lambda x: x*10, [1,2,3,4,5])
    return x

def listeYap(x):
    y=list(x)
    return y

#print(listeYap(onIleCarp()))

#örnek-3:
#parametre olarak dosya ismini alan
#noktadan önce ve sonrasını ayırıp (bölme işlemi)
#noktadan öncesini büyük harfle yazdıran fonksiyonu yazınız

def noktaAyir(x):
    y=x.split(".")
    return y

def dosyaAdi(x):
    y=noktaAyir(x)[0].upper()
    return y

def dosyaOku(x):
    with open(x,"r") as f:
        y=f.read()
        return y

#print(dosyaOku("C:/Users/eymen/Desktop/deneme.txt"))

#print(dosyaAdi(dosyaOku("C:/Users/eymen/Desktop/deneme.txt")))


#örnek-4:
#listedeki elemanlardan uzunluğu 4 veya 4'ten büyük olan elemanları filter ile bul
#bulunan elemanları ekrana yazdır

def elemanBul(x):
    y=filter(lambda x: len(x)>=4, x)
    return y

def listeYap(x):
    y=list(x)
    return y

#print(listeYap(elemanBul(["ali","ela","veli","ayse","fatma","mehmet","ahmet","ilker"])))
