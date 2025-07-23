# Nested Condition
hasRice = True
hasSpoon = True
if hasRice:
    print("มีข้าว")
    if hasSpoon:
        print("มีช้อน")
        print("กินข้าวได้")
    else:
        print("มีแต่ข้าวไม่มีช้อนจะกินยังไง")
else:
    print("ไม่มีข้าว ขอขยะกินหน่อยครับ")

# for loop
for i in range(5):
    print("Hello",i)

for i in range(1,5):
    print("Hello",i)

for i in range(1,10,2):
    print(i)

box = 0
for i in range(10):
    print(box+i)
   # box = box+i
    box += i
print("ค่าของbox :",box)

num = int(input("ป้อนจำนวนรอบ :"))
sum = 0
for i in range(1,num+1):
    sum += i
    print("วนรอบที่",i,":",sum)

# While loop
while True:
    inp = float(input("input number :"))
    if inp == 7.00:
        break

i = 0
while i < 5:
    i+=1
    print(i)

