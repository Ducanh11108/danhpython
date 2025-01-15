# Bài Tập 5: Viết 1 trương trình python thực hiện đổi chỗ

import math   

a = 10 
b = 20

tg = a      ## cái này thực hiện đổi chỗ
a = b
b = tg

a, b = b, a      #Cách đổi chỗ kiểu khác

print(a, b)