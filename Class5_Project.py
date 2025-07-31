menu = [
    {"id": 1, "fav": "Classic", "price": 30},
    {"id": 2, "fav": "Chocolate", "price": 45},
    {"id": 3, "fav": "Strawberry", "price": 50}
]

fav = []

print("Welcome to LungPond Square - Favor list\n---------------------------------------")
for m in menu:
    print(m["id"], m["fav"], m["price"], "Bath")

def orders():
    while True:
        try:
            order = int(input("Choose your number of favors: "))
            for i in menu:
                if i["id"] == order:
                    fav.append(i)
                    return i['price']
            print("not in menu")
        except ValueError:
            print("input must be a number, please try again.")
       
def main(): 
    total = 0
    while True:
        total += orders()
        add = input("สั่งอีกไหม (y/N): ").strip().lower()
        if add != 'y':
            break

    print("Odered list\n------------------------------")
    for i in fav:
        print(i['fav'], i['price'], "Bath")
    print("Total",total, "Bath")
main()