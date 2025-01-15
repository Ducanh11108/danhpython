# Bài Tập 2: Viết phương trình Python tính thể tích của hình lập phương.

# V lap phuong = a * a * a = a ^ 3

import math as mt

a = float(input("Nhap vao canh cua hinh lap phuong: "))

v = round(mt.pow(a, 3), 2)

print("The tich hinh lap phuong la: " + str(v))