# Bài Tập 1

import math

x = 0.501

f = pow(math.e, x) - x

f1 = math.e ** x - x   #Cách khác và cho ra kết quả tương đương
print(f)

print(round(f, 2))            #Dùng round để làm tròn

print(f, f1)