"""

เขียนโปรแกรม ของโปรแกรมค านวณค่าไฟฟ้าที่ใช้ภายในบ้าน แล้วแสดงผลค่าไฟฟ้าค านวณได้ทางหน้าจอ ทั้งนี้รูปแบบ
การใช้งานโปรแกรมให้รับบ้านเลขที่ และจ านวนหน่วยไฟฟ้าที่ใช้ไปทางแป้นพิมพ์ 
 โดยในการคิดค านวณค่าไฟฟ้า คิดหน่วยละ 5.00 บาท ส าหรับกรณีที่ใช้ไฟฟ้าไม่เกิน 20 หน่วย แต่หากใช้เกิน 
20 หน่วย แต่ไม่ถึง 50 หน่วยจะลดราคาลงคิดเพียงหน่วยละ 4.50 บาท และหากใช้ตั้งแต่ 50 หน่วยขึ้นไปจะลดราคาลง
คิดเพียงหน่วยละ 4.00 บาท 
 ก าหนดหน้าจอการแสดงผลเบื้องต้นให้ ดังนี้ 
------------------------------------------------
 Program Pay Electric
------------------------------------------------
Enter home number : <input>
Enter unit of electric : <input>
------------------------------------------------
Pay for electric use is : <output>
------------------------------------------------
กาหนดให้มีฟังก์ชันในการท างานอย่างน้อย 2 ฟังก์ชันอะไรก็ได

"""

def line():
    print("--------------------------------")

def rateForPay(unit):
    if unit <= 20:
        rate=5.00
    elif unit < 50:
        rate=4.50
    elif unit >= 50:
        rate=4.00
    return unit*rate

def payElectric():
    line()
    print("Program Pay Electric")
    line()
    homeNumber = int(input("Input Your Home Number: "))
    unitForPay = float(input("Input Unit: "))
    total = rateForPay(unitForPay)
    print(f"บ้านเลขที่:{homeNumber} มีค่าใช้จ่าย: {total}")
    line()

payElectric()
