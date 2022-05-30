#örnek 1:
#elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin olduğu bir liste olsun
#define a list of pairs of numbers denoting the sides of a rectangle
#[(3,4),(10,3),(5,6),(1,9)]
#şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazınız
#now write a function that calculates the area of the rectangle based on the side lengths
#ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.
#and apply this function to each element of this list and print a list like this.
#[12, 30,30,9]
from functools import reduce

x=[(3,4),(10,3),(5,6),(1,9),(2,3)]

def area(x):
    return x[0]*x[1]

def writeListWithMap(x):
    return list(map(area,x))

#print(writeListWithMap(x))


#örnek 2:
#her bir elemanı 3'lü bir demet olan bir liste tanımlayın
#define a list of triplets of numbers
#[(3,4,5),(10,3,9),(5,6,7),(1,9,8)]
#şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın
#now write a function that returns whether or not a triangle can be made with the given side lengths
#ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.
#and print the list of triangles that can be made with the given side lengths.

a= [(3,4,5),(6,8,10),(3,10,7),(1,9,8),(2,3,4)]

def isTriangle(x):
    return x[0]+x[1]>x[2] and x[1]+x[2]>x[0] and x[0]+x[2]>x[1]

def writeListWithFilter(x):
    return list(filter(isTriangle,x))

#print(writeListWithFilter(a))

#örnek 3:
#isim ve soyisimlerin bulunduğu iki tane lista tanımlayın
#define two lists of names and surnames
#['John', 'Smith', 'Mary', 'Williams', 'Mike', 'Jones']
#['Smith', 'Williams', 'Jones', 'John', 'Mike', 'Mary']
#şimdi isimlerin ve soyisimlerinin birleştirilmiş halini dönen bir fonksiyon yazın
#now write a function that returns the combined name and surname
#ve bu listeyi ekrana yazdırın.
#and print the list of combined names and surnames.

a=['kerem', 'tuğçe', 'ezgi', 'kemal', 'ilkay', 'şükran']
b=['yılmaz', 'öztürk', 'dağdeviren', 'atatürk', 'dikmen', 'kaya']

def birlestir(x,y):
    return x+" "+y

#print(list(zip(a,b)))

#örnek 4:
#elinizde şöyle bir liste olsun
#define a list of numbers
#[1,2,3,4,5,6,7,8,9,10]
#şimdi reduce ile bu liste içindeki çift sayıların toplamını dönen bir fonksiyon yazın
#now write a function that returns the sum of the even numbers in the list with reduce
#ve bu listeyi ekrana yazdırın.
#and print the list of even numbers.


sayilar=[1,2,3,4,5,6,7,8,9,10]

def ciftSayiToplami(x):
    return reduce(lambda x,y:x+y,x)

def ciftSayiBul(x):
    return list(filter(lambda x: x%2==0,x))

#print(ciftSayiToplami(sayilar))


