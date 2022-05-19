# ÇALIŞMA SORULARI VE CEVAPLARI
# 1.N sayının faktöriyelini alan programı (n sabit olarak düşünülebilir, gerekli kütüphanelerin import edildiğini varsayabilirsiniz
# fonksiyonel programlama araçları ile tek satırda yazınız.

from functools import reduce

n = 5
a = reduce(lambda a, b: a * b, [i for i in range(1, n + 1)])
print(a)

# not-1:  range içerisinde n+1 alınmasının nedeni, range fonksiyonunda bitiş parametresinin aralığa dahil olmamasıdır.
# not-2: aynı örnek lambda fonksiyonu ayrı bir sayırda yazılarak veya normal bir fonksiyon ile de yazılabilirdi

# 2. x=[“MerhaBA”, “PYTHON”, “pROGRAMLAMA”, “Dili”] gibi bir string dizisini “Merhaba Python Programlama Dili” şeklinde tek bir stringe dönüştürecek
# programı en fazla 3 satırda fonksiyonel programlama araçları ile yazınız.
# Yardımcı metotlar: title() => stringin baş harfini büyütür, ‘ ’.join(liste) parametre olarak aldığı listedeki stringleri
# tek tırnaklar içindeki karakteri kullanarak birleştirir.

x = ["MerhaBA", "PYTHON", "pROGRAMLAMA", "Dili"]
y = [i.title() for i in x]
print(' '.join(y))

# 3. ["kayak", "adana", "yapay", "kek","urfa","hatay"] gibi bir stringlerden oluşan listemiz olduğunu varsayarak, bu listedeki palindrom
# (tersten okunuşu kendine eşit olan) kelimeleri süzen(filtreleyen) programı tek satırda ve fonksiyonel programlama araçları kullanarak yazınız.
# (İpucu: string tersi için liste parçalamayı hatırlayınız, liste/stringler parçalanırken range benzeri üç parametre kullanılabilir)

x = ["kayak", "adana", "yapay", "kek", "urfa", "hatay"]
y = list(filter(lambda a: a == a[::-1], x))
print(y)


# not-1: sade gözükmesi için ayrı bir satırda yazılmıştır.
# not-2: kod bir list() içine alınmıştır çünkü filter() bir obje dönüş değerine sahiptir.

# 4. sıradaki fibonacci sayısını üreten fonksiyonel programlama kodunu nesne ve iter kullanarak ve next() metodunu ezerek (override) yazınız.
#sonlu bir iter sınıfı yazabilmek için gerekli parametreyi yapılandırıcıya gönderin.


class Fibo:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.f1, self.f2, self.i = [1, 1, 0]
        return self

    def __next__(self):
        while (self.i < 5):
            self.f1, self.f2 = [self.f2, self.f1 + self.f2]
            self.i += 1
            return self.f2
        else:
            raise StopIteration


x = Fibo(5)
x = iter(x)
print(next(x))

# 5. aşağıdaki programda ayrı ayrı veri yapılarında tutulan kullanıcı adları ve şifreler, fonksiyonel programlama
# yapıları ile tek satırda sözlük yağısında birleştirilmiştir. ilgili tek satırlık kodu yazınız.

usernames = ["ali", "veli", "fatma"]
passwords = ["123", "abc123", "23el23"]

soz = map(lambda a, b: {a: b}, usernames, passwords)
print(list(soz))

# 6. aşağıdaki programın ekran çıktısını yazarak, mantığını bir cümle ile açıklayınız.
x = [1, 2, 3, 4, 5];
x = iter(x)
s = 0
while True:
    try:
        s += next(x)
    except StopIteration:
        break
    finally:
        print(s)

# 7. bir listeyi iterable hale getirerek sonsuz bir döngü yapısı içinde istisna işleme kullanarak tembel değerlendirme ile elemanlarını toplayan
#python kodunu yazınız.


# 8. aşağıdaki programı bir satırla açıklayarak, z ile oluşacak ekran çıktısını tam olarak yazınız.

x = [1, 2, 3, 256]
y = [2, 3, 3, 0.5]

z = list(map(lambda a, b: int(a * b), x, y))
print("soru 8 çıktısı: ", z)

# soru 8 için oluşacak ekran çıktısı: [2, 6, 9, 128]


# 9. Sayılardan oluşan iki liste olduğunu varsayarak bunları karşılıklı olarak 3. bir listede ilk listedeki elemanlar taban,
# ikinci listedeki elemanlar üs olacak şekilde birleştiren kodu fonksiyonel programlama kullanarak tek satırda yazınız.
