#Bài Tập 1:  Viết chương trình Python tính thể tích của một hình cầu.

# V hinh cau = 4/3 * pi * r ^ 3

import math as mt 

r = float(input("Nhap ban kinh hinh cau: "))

v = (4/3 * mt.pi * mt.pow(r, 3), 2)

print("The tich hinh cau la: " + str(v))
