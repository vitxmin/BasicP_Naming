monster = 100
knife = 15
sword = 35
gun = 50
result = 0

while True:
    choose = int(input("เลือก1เพื่อสู้ เลือก2เพื่อออกจากเกม :"))
    if choose == 2:
        print("end")
        break
    elif choose == 1:
        round = int(input("เลือกจำนวนรอบที่จะตี :"))
        i = 0
        while i<round:
            i+=1
            choosewp = int(input("เลือกอาวุธ1.knife = 20,2.sword = 35,3.gun = 50 :"))
            if choosewp == 1:
                monster -= knife
            elif choosewp == 2:
                monster -= sword
            elif choosewp == 3:
                monster -= gun
            if monster < 0:
                monster = 20
            print("เลือดมอนเตอร์เหลือ :",monster)
            
            
        
  

