#ĐỀ THI TIN 
#Bài 1: Trò chơi[GAME]
# Bạn đang tham gia một trò chơi như sau: có 2 nút bấm A và B, trên nút A ghi số MA, trên nút B ghi số MB. Ở mỗi lượt chơi, bạn phải chọn bấm một trong 2 nút và sẽ nhận được số
# điểm thưởng bằng với số ghi trên nút đó, sau đó số ghi trên nút vừa bấm sẽ giảm đi một đơn vị. Hỏi rằng sau 2 lượt chơi, số điểm thưởng lớn nhất mà bạn có thể nhận được là bao nhiêu?

# DỮ LIỆU
# -Một dòng duy nhất ghi 2 số nguyên dương MA, MB (3<=A, B <= 20) tương ứng với số ghi trên nút A và nút B;

#KẾT quả
# - Ghi số điểm thưởng lớn nhất mà bạn có thể nhận được sau 2 lượt chơi.

#Bài Làm

a = int(input("a = "))
b = int(input("b = "))
mostpoint = 0
if(a > b):
    if(a - 1 > b):
        mostpoint = a - 1 + a
    else: mostpoint = a + b
elif(b > a):
    if(b - 1 > a):
        mostpoint = b - 1 + b
    else: mostpoint =  a + b   
else: mostpoint = a + b
print(mostpoint)                     
