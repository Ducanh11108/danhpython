s = "Hello how are you"

print(s[6])     #Đếm lhoangr cách kí tự: vd: 6 thì khoảng cách thứ 6 là chữ h

print(s[-1])    #Khoảng cách -1 sẽ rơi vào chữ u

#Truy cập theo chiều thuận từ trái qua phải đếm từ 0
#Truy cập theo chiều từ phải sang trái đếm từ 1

print(s[-5])

# <tenBienChuoi>[<start>:<end>:<step>]
print(s[0:5:1])

s1 = "Hello"
s2 = "C" + s[1:5]

print(s1[5:2:-1])
print(s1[5:1:-1])

print(s2)