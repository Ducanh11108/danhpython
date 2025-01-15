# Các phép toán thao tác bit cơ bản
# Phép toán AND (&)
# Phép toán OR (|)
# Phép toán XOR (^)
# Phép toán NOT (~)
# Toán tử dịch bit
# Dịch phải (>>)
# Dịch trái bit (<<)

a = 10
b = 2

print(a & b)
# số 10 đổi sang nhị phân là 1010
# số 2 đổi sang nhị phân là 0010
# Phep&bit    res(kết quả)
#1       1     1
#1       0     0
#0       1     0
#0       0     0
# vậy kết quả 0010 là 2

print(a | b)
#Phep | bit       res(kết quả)
#  1     1          1
#  1     0          1
#  0     0          0

#1010
#0010
# tính từ phải qua trái
# ta có 1 hoặc với 1 thì có kết quả là 1
# ta có 0 hoặc với 1 thì có kết quả là 0
# ta có 1 hoặc với 1 thì có kết quả là 1
# ta có 0 hoặc với 1 thì có kết quả là 0
# Như vậy ta có kết quả là 1010 và bằng 10

print(a ^ b)
#Phep^bit     res(kết quả)
#  1    1         0          (Ta có 1 so với 1 thì kết quả là 0)
#  1    0         1          (Ta có 1 so với 0 thì kết quả là 1)
#  0    1         1          (Ta có 0 so với 1 thì kết quả là 1)
#  0    0         0          (Ta có 0 so với 0 thì kết quả là 0)

#1010                    10
#0010                     2
#1000 ( vậy ta đc kqua)   8
#1000 đổi sang nhị phân bằng 8


a = 10
b = 2  # - (n+1) = -(2+1) =-3
#Phủ định của 2 = -3
# => Công thức phủ định của -n là:  -(n+1)

print(~b)

print(a << 1)

# 10 đổi sang là 1010
# Như vậy tiến sang 1 bit sẽ là 20 (đếm từ trái qua phải) 
# => đáp án là 10100 đổi sang nhị phân = 20


#Dịch phải cũng tương tự 
a = 10 >> 2  # 10 chia 2 = 5
b = 1 << 10

print(b)