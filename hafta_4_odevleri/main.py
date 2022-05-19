def odev1():#find prime numbers
    print("Ödev 1:")

    s = int(input("Sayı girin: "))
    f = 0
    i = 2
    while i <= s / 2:
        if s % i == 0:
            f = 1
            break
        i = i + 1
    if f == 0:
        print("Asal Sayıdır")
    else:
        print("Asal Sayı Değildir")

def odev2():
    print("Ödev 2:")
    #Generate 100 numbers in the range of 0-10 and
    #find out how many times each number repeats
    import random
    liste = []
    for i in range(100):
        liste.append(random.randint(0,100))
    print("Liste: ",liste)
    for i in range(10):
        print(i, ":", liste.count(i))


def odev3():
    print("Ödev 3:")
    #Find 100 numbers in the 0-1 range and find the smallest number, the largest number, the mean, the median, and the standard deviation.
    import random
    liste = []
    for i in range(100):
        liste.append(random.random())
    print("Liste: ",liste)
    print("En küçük: ",min(liste))
    print("En büyük: ",max(liste))
    print("Ortalama: ",sum(liste)/len(liste))
    print("Medyan: ",liste[49])
    print("Standart Sapma: ",sum(liste)/len(liste))

def odev4():
    print("Ödev 4:")
#Generate 10 numbers in the range a-b with random.random()

odev1()
odev2()
odev3()
odev4()

def findMinNumberInList(liste):
    min = liste[0]
    for i in liste:
        if i < min:
            min = i
    return min

def findMaxNumberInList(liste):
    max = liste[0]
    for i in liste:
        if i > max:
            max = i
    return max

def findMeanOfList(liste):
    return sum(liste)/len(liste)

def findMedianOfList(liste):
    liste.sort()
    return liste[len(liste)//2]

def findStandardDeviationOfList(liste):
    return sum(liste)/len(liste)

def findAverageOfList(liste):
    return sum(liste)/len(liste)

# 21.03.2020 labaratuvar
dikKenar1= int(input("Dik kenar 1: "))
dikKenar2= int(input("Dik kenar 2: "))
hipotenus= (dikKenar1**2 + dikKenar2**2)**0.5
print("Hipotenüs: ",hipotenus)

#kullanıcıdan alınan iki sayının değerlerini birbiriyle değiştirip ekrana yazdırın.
def degerDegistir():
    sayi1 = int(input("Sayı 1: "))
    sayi2 = int(input("Sayı 2: "))
    print("Sayılar: ",sayi1,sayi2)
    sayi1,sayi2 = sayi2,sayi1
    print("Sayılar: ",sayi1,sayi2)


degerDegistir()

#üçgenin alanını hesaplayın.
def ucgenAlan():
    kenar1 = int(input("Kenar 1: "))
    kenar2 = int(input("Kenar 2: "))
    kenar3 = int(input("Kenar 3: "))
    alan = kenar1*kenar2*kenar3
    print("Alan: ",alan)

ucgenAlan()

#öklid mesafesi hesaplayın.
def oklidMesafe():
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    mesafe = ((x1-x2)**2 + (y1-y2)**2)**0.5
    print("Mesafe: ",mesafe)

oklidMesafe()


