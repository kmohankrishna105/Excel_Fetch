"""

class C1():
    pass

def sum(a,b):
    return a+b
print(dir())

x=C1()
print(C1)
print (x)

print (type(x))

Typeclass=type("Typeclass",(),{'x':5,'Ph':sum(12,3)})

t=Typeclass()
print (type(t.Ph))

print(t.__class__)


j={'f':[]}
g={1:2,3:4,5:6}
j['f'].append(g)
print (j)

print (type(t).__name__)

class Cname(object):
    def Cnamem1(self):
        return "c"

    class Cnamec:
        pass

    c=Cnamec

c2=Cname()
print(type(c2))

#Yield:

def square():
    i = 1
    while True:
        i = i + 1
        yield i*i

for num in square():
    if num >200:
        break
    print(num)

#Return:

def square1():
    i = 1
    lis=[]
    for i in range (1,20):
        if i<10:
            sqr = i*i
            i = i + 1
            lis.append(sqr)
    return lis

for num in square1():
    if num >200:
        break
    print(num)

"""

from decimal import Decimal
h=195
"""
def convert_strikeprice(price):
    print(type(h))
    print (round(h,2))
    d =Decimal(round(h,2))
    p=abs(d.as_tuple().exponent)
    print (p)
    if type(h)==int:
        return (h)
    else:
        if p<2:
            print (str(d)+'0')
        else:
            print(str(round(h,2)))
"""

def convert_strikeprice(price):
    if type(price)==int:
        return (price)
    else:
        d = Decimal(round(price, 2))
        p = abs(d.as_tuple().exponent)
        print (p)
        if p<2:
            return (str(d)+'0')
        else:
            return (str(round(price,2)))

print(convert_strikeprice(195.5))

