"""
#fibonachi recursive yazınız
def fib1(n):
    return 1 if n<=1  else fib1(n-1)+fib1(n-2)

print(fib1(5))
"""

from functools import reduce
a="abcdefgh"
b=reduce(lambda a,b: a.upper()+b.lower(), list(a.strip(' ')))

print(list(a.strip(' ')))
print(b)

print()