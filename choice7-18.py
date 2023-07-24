# ข้อ 7

def f1(a,b):
    return a+b, a // b
def f2(a,b):
    return a-b, a / b

x = float("7.0")
y = int("3")

if x%y > 1:
    x,y = f1(x,y)
else:
    x,y = f2(x,y)

print(f"{x:.2f},{y:.2f}")

# ตอบ ข. 4.00,2.33

# ข้อ 8

def foo1(y):
    x = y + 8
def foo2(x,y):
    y = x + 2
    return y

x = 3
y = 5
foo1(x)
print(x)
x = foo2(x = y, y= x)
print(x)

# ตอบ ก. 3,7

# ข้อ 9 
print(4 * 20 / 8 % 7 - 2 ** 3)

# ตอบ ก.

# ข้อ 10

# ตอบ ข.2 (4 * 2 + 4 * 2) = 32

# ข้อ 11

def func(x,y):
    x = x*10
    y = y*10
    return y -x
x,y = 1,2
y =func(3,4)
print(f"{x},{y}")
#ตอบข้อ ข. 1,10

# ข้อ 12
# ข้อใดไม่มี Eror
false = True

# ตอบ ก. เพราะ false ที่มีพิมเล็กขึ้นต้น จะสามารถตั้งเป็นตัวแปรได้ แต่ถ้า  False แบบนี้ จะเป็น Boolean แล้ว eror

# ข้อ 13

y = 300
print(y//2%3//2)

# ตอบ ก. 0 เพราะ 300 // 2 = 150 % 3 = 50  // 2 =0

# ข้อ 14

x = 16-2*5//3+1
print(x)
# ตอบ ข. 14 เพราะ 2*5 = 10 // 4 = 2.5 = 16-2.5 = 14.5

# ข้อ 15
y = 2**5+2*5<0
print(y)

# ตอบ ข. เพราะ ถ้ามี <> = != เท่ากับผลลัพธ์จะเป็นค่า boolean True หรือ False เท่านั้น

# ข้อ 16
val = 20
def change_to_ten():
    val = 10
    val = val+1
change_to_ten()
print(val)
# ตอบ ค. เพราะ ฟังชั่น change_to_ten แค่ใช้เก็บค่า แต่ไม่ได้ output ออกมา
# เลยแสดงผลแค่ ตัวแปร val ที่มีค่า = 20

# ข้อ 17
def myf():
    y = 4
    z = y+x
    return z
x,y = 9,7
x = myf()
print(x,y)

#  ตอบ ค. 13 7 เพราะ x = ฟังชั่น myf ที่ return ค่า z = y+x
#  =4+9 = 13 ส่วนค่าคือ 7 ที่มาจากตัวแปร x,y = 9,7

# ข้อ 18

def f1(b):
    if b > a:
        return b
    else:
        return a*2

def f2(b,a):
    if a+b > 10:
        return(f1(a))
    elif b - a < 0:
        return b
    if a < 0:
        return -a
    return a

a = int(input())
print(f2(a,f1(f1(a))))