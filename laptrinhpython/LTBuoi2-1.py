S = "    Hoc Cong Nghe"

print(type(S))

#capitalize() Viet hoa chu dau tien trong chuoi

print(S.capitalize())

# upper() Chuyen chuoi sang chu in hoa
print(S.upper())

#lower() Chuyen chuoi tu chu hoa sang chu thuong

print(S.lower())

#title() Chuyen ky tu dau moi tu sang in hoa

S = "a  hoc cong nghe"

print(S.title())

# strip() Xoa ky tu duoc chi dinh o dau va cuoi chuoi
print(S.strip())

# lstrip() Xoa ky tu duoc chi dinh o ben trai chuoi
print(S.lstrip("a"))

# split() Tach cac ky tu trong chuoi 
# Chuoi.split(char, n)

s1 = "Xin chao cac ban"

print(s1.split())

# count() Dem so lan xuat hien cua mot chuoi con trong chuoi goc
s2 = "how are you i am Ducanh"

print(s2.count("how",0, 11))

# find() Tim chuoi con trong chuoi goc, neu khong tim duoc thi tra ve -1
print(s2.find("how",0, 4))

# join Noi chuoi
# Ky_tu_noi.join(tham_so)

x = ["Hoc", "Cong", "Nghe"]

y = " ".join(x)

print(y)

# replace() Thay the mot chuoi con trong chuoi goc

t = "Xin chao cac ban den voi khoa hoc lap trinh Python"

print(t.replace("khoa", "lop"))