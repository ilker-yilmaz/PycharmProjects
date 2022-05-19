import random
print("***********************************")
print("----------- SAYISAL LOTO ----------")

#bizim tahminlerimiz
tahmin1= int(input("1. Tahmininizi Giriniz: "))
tahmin2= int(input("2. Tahmininizi Giriniz: "))
tahmin3= int(input("3. Tahmininizi Giriniz: "))
tahmin4= int(input("4. Tahmininizi Giriniz: "))
tahmin5= int(input("5. Tahmininizi Giriniz: "))
tahmin6= int(input("6. Tahmininizi Giriniz: "))

#rastgele oluşturulan sayılar
rasgele1=random.randint(1,49)
rasgele2=random.randint(1,49)
rasgele3=random.randint(1,49)
rasgele4=random.randint(1,49)
rasgele5=random.randint(1,49)
rasgele6=random.randint(1,49)

print("----------- SAYISAL LOTO SONUÇLARI ----------")
print("s1","s2","s3","s4","s5","s6")
print(rasgele1," ",rasgele2,"",rasgele3,"",rasgele4,"",rasgele5,"",rasgele6)

print("----------- TAHMİNLERİNİZ ----------")
print("T1","T2","T3","T4","T5","T6")
print(tahmin1," ",tahmin2,"",tahmin3,"",tahmin4,"",tahmin5,"",tahmin6)

print("----------- SONUÇLAR ----------")
bakiye=0
if(tahmin1==rasgele1):
    print("1. tahmin doğru", "KAZANDINIZ...")
    bakiye1=5
else:
    print("1. tahmin yanlış", "KAYBETTİNİZ...")
    bakiye1=0

if(tahmin2==rasgele2):
    print("2. tahmin doğru", "KAZANDINIZ...")
    bakiye2=10
else:
    print("2. tahmin yanlış", "KAYBETTİNİZ...")
    bakiye2=0

if(tahmin3==rasgele3):
    print("3. tahmin doğru", "KAZANDINIZ...")
    bakiye3=15
else:
    print("3. tahmin yanlış", "KAYBETTİNİZ...")
    bakiye3=0

if(tahmin4==rasgele4):
    print("4. tahmin doğru", "KAZANDINIZ...")
    bakiye4=20
else:
    print("4. tahmin yanlış", "KAYBETTİNİZ...")
    bakiye4=0

if(tahmin5==rasgele5):
    print("5. tahmin doğru", "KAZANDINIZ...")
    bakiye5=25
else:
    print("5. tahmin yanlış", "KAYBETTİNİZ...")
    bakiye5=0

if(tahmin6==rasgele6):
    print("6. tahmin doğru", "KAZANDINIZ...")
    bakiye6=30
else:
    print("6. tahmin yanlış", "KAYBETTİNİZ...")
    bakiye6=0

bakiye=bakiye1+bakiye2+bakiye3+bakiye4+bakiye5+bakiye6
print("Toplam Kazancınız: ",bakiye,"TL")

print("***********************************")
