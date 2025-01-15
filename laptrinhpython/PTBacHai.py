# Bài Tập 2: Giải và biện luận phương trình bậc 2


# ax^2 + bx + c = 0
#Neu a != 0 ( != đc hiểu là khác không): 
      # -Neu delta > 0 thi phuong trinh co 2 nghiem phan biet
      #x1 = (- b + sqrt(delta)) / (2 * a)
      #x2 = (- b -sqrt(delta)) / (2 * a)
      # -Neu delta = 0 thi phuong trinh co nghiem kep:
      # x1 = x2 = -b / (2 * a)
      # -Neu delta < 0 thi phuong trinh vo nghiem

#Neu a == 0:
    #Giai bien luan phuong trinh bac nhat
import math

a = input("a = ")
b = input("b = ")
c = input("c = ")

a = float(a)-1
b = float(b)
c = float(c)

if(a != 0):
    delta = b * b - 4 * a * c
    if(delta > 0):
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("x1 =", x1, " x2 =", x2)
    elif(delta == 0):
        x1 = x2 = -b / (2 * a)
        print("x1 = x2 =", x1)
    else:
        print("Phuong trinh bac 2 vo nghiem")
else:    
        if(b != 0):
            print("x =",-c / b)
    
        if(c == 0):
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")       
        
