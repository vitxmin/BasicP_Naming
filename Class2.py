# Data type
# 1.int
age = 18 
money = -200 
zero = 0

print(type(age))
print(type(money))
print(type(zero))

# 2.float
weight = 12.12 
profit = -0.9
zero = 0.00 

print(type(weight))
print(type(profit))
print(type(zero))

# 3.bool
cat = True
dog = False
isCat = True

print(cat)
print(dog)
print(isCat)

# 4.str
hello = "Hello World"
phone = "063"
call = "I'm Stitch"

print(hello)
print(phone)
print(call)

# Type Conversion
# str --> int
cost = "200"
print(int(cost)+50)
# int --> str
num = 888
print("SIT"+str(num))
# float --> int
jud = 12.12
print("This is MaiChaiJud:",int(jud))

# exercise
a = "120"
b = "180"
print("a + b =",int(a)+int(b))

# float
teddy = 15
print(float(teddy))

# upper
bear = "big bear"
print(str.upper(bear))

# Operators
print(20+10)
print(20-10)
print(20*10)
print(10/3)
print("10 % 3 =",10%3)
print("10 % 2 =",10%2)
print(20**10)
print("Hello"+" "+"World")
print("Hello"*3)

# Comparison Operators
# == , != , < , > , >= , <=

o1 = 5
o2 = 10
print(o1 == 5)
print(o1 == o2)
print(o1 != o2)
print(o1 < o2)
print(o1 > o2)
print(o1 >= o2)
print(o1 <= o2)
print(o2>10)

print("Bool")
# Boolean Operators
# and , or , not
p = True
q = False
print(p and q) # false
print(q and q) # false

print(p or q) # true
print(p or p) # true

print(not True) # false
print(not False) # true



whatUp = input("My name is : ")
print("Hello",whatUp,"Have a nice day")

pton_is_itim = True
pton_aroi = True
pton_cheap = False
if pton_is_itim and pton_aroi:
    print("eat p'ton")
elif pton_cheap:
    print("eat p'ton bc cheap")
else:
    print("GoHome")


