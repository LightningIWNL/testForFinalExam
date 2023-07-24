#ข้อ 1
m = 5
n = "Hel"
i = "HelHel"
p = 8
q = 3

def test01():
    if (p > 0) or not (p <= 0) or (n * q == n + i) :
        print(True)
    else:
        print(False)

test01()

#ตอบ ง. (p > 0) or not (p <= 0) or (n * q == n + i)

#ข้อ 2

def me(m):
    if (m<0):
        print("Level 1")
    elif (m>15):
        print("Level 2")
    elif (m<50):
        print("Level 3")
    elif (m<60):
        print("Level 4")
    elif (m==0):
        print("Level m")
        
n = 0
me(m=n)
# ตอบ ข. Level2
# คำตอบสามารถเป็น Level 3 หรือ 4 หรือ m เพราะ m มีถูกกำหนดค่าให้เป็น 0 แต่คำสั่ง if ตรวจสอบเจอ Level 2 ก่อน คำตอบเลยเป็น ข.Level 2

# ข้อ 3

z = 2 ** 3 ** 2 // 10 +123 % 2
print(z)

# ตอบ ง. 52

# ข้อ 4

def increaseM(x):
    x = x+1
    return x
    print(x)
    
x=9
print(x)
increaseM(x)
print(x)

# ตอบ ก. 9 9
# เพราะ x ถูก return ค่าไปที่ parameter ก่อนถึง print เลยทำให้ คำสั่งไม่มีค่าใดๆ

# ข้อ 5

val1 = "one"
val2 = "all"
print("{val1}"+int(4)*val2)

# ตอบ ข้อ ง. {val1}allallallall
# เพราะไม่ได้ใช้ f-string {val1} ที่ควรจะเป็นคำสั่ง output ตัวแปร เลยถูก output  ออกมาเป็นข้อความแทน

# ข้อ 6
a =14
mark = True
if((a>4)and not mark):
    print("Ant")
    if(mark or 25<a):
        print("Bee")
else:
    if(not(5<a or a>40)):
            print("Cat")
    if(a != 4 and a == 14):
            print("Dog")

# ตอบ ง. Dog

# ข้อ 7

