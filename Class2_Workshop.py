km = int(input("Input km :"))
price = 0
if 5 <= km <= 50:
    price = 10
elif 51 <= km <= 100:
    price = 15
elif 101 <= km <= 300:
    price = 25
elif 301 <= km <= 500:
    price = 35
elif km > 500:
    price = 45
else:
    price = 0
    print("ไม่ส่งเว้ย")

vat = price*0.07
print("Before Vat :",price,"baht")

#เสริมนอกโจทย์
print("Total +Vat7% :",price+vat,"baht")
