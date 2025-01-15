# ax + b = 0

#1. Neu a <> 0 -> x = -b/a
#2. Neu a = 0:
#   Neu b = 0 -> x = vo so nghiem
#   Neu b != 0 -> x = vo nghiem

a = float(input("a ="))
b = float(input("b ="))
x = 0
if(a !=0):
    x = -b / a
    print("x =", -b/a)
else:
    if(b == 0):
        print("Phuong trinh co vo so nghiem")   
    else:
        print("Phuong trinh vo nghiem")     