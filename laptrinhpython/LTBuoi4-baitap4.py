# Bài Tập 4

import math
s = input("Input a string: ")

res = ""    #(chuỗi kết quả)

if len(s) < 2:     #(Độ dài của s nhỏ hơn 2)  
     res = ""
else:      #(lấy e kí tự đầu và cuối) 
     s1 = s[0:2]
     s2 = s[-2:]
     res = s[0:2] + s[-2:]

print(res)       