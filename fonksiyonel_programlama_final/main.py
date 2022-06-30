#soru-1
#öncelikle string cümleyi alıp split ile değerlerine ayırıyordu
#daha sonra bu değerleri tek tek kontrol edip
#uzunluğu 3ten küçük olanları direkt yazdırıyordu
#büyük olanları da tersine çeviriyordu


#soru-2
from functools import reduce

x = map( lambda a : a [::-1] if len(a) > 3 else a,  "Why i do love Python?".split(" "))
print(list(x))

#soru-3
print(reduce(lambda a,b:a**b , range(-1,6,2)))

#soru-4


#soru-5
print(reduce(lambda a,b:a**b , range(-1,6,2)))