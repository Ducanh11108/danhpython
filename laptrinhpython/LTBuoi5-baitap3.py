# Xep loai hoc sinh
#Neu dtb < 5 -> Yeu
#Neu dtb >= 7 and dtb < 8 -> Kha
##Neu dtb >= 9 -> Xuat sac


dtb = float(input("Nhap vao diem tb cua ban: "))

if(dtb < 5):
    print("Xep loai YEU")
elif(dtb >= 5 and dtb < 7):
    print("Xep loai TRUNG BINH")
elif(dtb >= 7 and dtb < 8):
    print("Xep loai KHA")
elif(dtb >= 8 and dtb < 9):
    print("Xep loai GIOI")
else:
    print("Xep loai XUAT SAC")        