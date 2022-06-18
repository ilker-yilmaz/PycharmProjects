
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

#print(list(x))


# filter

x = list(range(10))

f = lambda a: a % 2 == 0

s = filter(f, x)
# print(list(s))


# reduce


from functools import reduce

f = lambda a1, a2: a1 + a2

s = reduce(f, [1, 2, 3, 4])

#print(s)


# faktöriyel örneği

from functools import reduce

f = lambda a1, a2: a1 * a2
s = reduce(f, range(1, 5))
# print(s)

import os

print(os.getcwd())

def fib2(n):
    if n<=1:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)

print(fib2(5))

fs=dict()

def fib(n):
    if n<=1:
        fs[str(n)]=1
        return 1
    elif str(n-1) in fs:
        fs[str(n)]=fs[str(n-1)] + fs[str(n-2)]
        return fs[str(n)]
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))

ilker=["a",1,2,3,"b","c",4,5,6]
print(type(ilker))
print(str(ilker))
ahmet=[i for i in ilker if str(i).isdigit()]


print(ahmet)