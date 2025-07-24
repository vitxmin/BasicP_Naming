# # Function
# # hello
# def hello():
#     print("Hello World")

# hello()

# # add
# def add(a,b):
#     print(a+b)

# add(12,20)
# add(7,10)
# x = 15
# y = 15

# introduction
# def introduction(fname):
#     print("My Name Is :",fname)
#     tellAge()
# # tellAge
# def tellAge():
#     age = input("Enter your age :")
#     print("Your age is :",age)

# introduction("Naming")

# def spam(name):
#     for s in range(5):
#         print(name)

# spam("Naming")

# def spam(name):
#     round = int(input("วนกี่รอบ :"))
#     for s in range(1,round+1):
#         print(name,s)

# spam("Naming")

# x = ["PangPond","Ton",2,7]
# sum = x[2]+x[3]
# print(sum)
# x[2] = 3
# sum = x[2]+x[3]
# print(sum)

# x[2] = "Naming"
# print(x)

# x = ["PangPond","Ton",2,7]
# print(x)
# x[2] = "Naming"
# x.append("Best")
# x.append(12.12)
# x.pop(3)
# x.pop(4)
# print(x)

# list = ["PangPond","Ton",2,7]

# for i in list:
#     if i == 2:
#         print("found 2")

# Dictionary
# members_rahus = {
#     "Name":"Naming",
#     "Rahus":"IT31"
# }
# print(members_rahus["Name"])

# dict_a = {
#     "sword":80,
#     "gun":70
# }
# dict_a["sword"] = 20
# dict_a["bow"] = 35
# print(dict_a)


def checkPrice(list_of_stores):
    for store in list_of_stores:
        if store["price"] == 250:
            print("ราคามากกว่า 200 --> แพงงงง")
        elif store["price"] == 45100:
            print("ราคาเท่าค่าเทอมไอที --> แพงโคตรแพงshiftหาย")
        else:
            print("ราคาน้อยกว่า 200 --> ถูกกกกก")

stores = [
    {"name":"Egg","id":10,"price":100},
    {"name":"Sugar","id":11,"price":250},
    {"name":"IT","id":12,"price":45100}
]
checkPrice(stores)
    

# dict_a = {
#     "name":"Egg",
#     "price":10
# }
# dict_b = {
#     "name":"Sugar",
#     "price":15
# }
# list = [dict_a,dict_b]
# print(list)

# for i in list:
#     print(i["price"])
