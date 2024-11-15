import math

def calculator():
    print("เครื่องคิดเลข")
    print("เลือกฟังก์ชันที่ต้องการ:")
    print("1. บวก (+)")
    print("2. ลบ (-)")
    print("3. คูณ (*)")
    print("4. หาร (/)")
    print("5. ยกกำลัง (^)")
    print("6. รากที่สอง (√)")
    print("7. ออกจากโปรแกรม")
    
    while True:
        choice = input("\nกรุณาเลือกฟังก์ชัน (1-7): ")
        
        if choice in ["1", "2", "3", "4", "5"]:
            # รับตัวเลขสองจำนวน
            num1 = float(input("กรอกตัวเลขตัวแรก: "))
            num2 = float(input("กรอกตัวเลขตัวที่สอง: "))
            
            if choice == "1":
                result = num1 + num2
                print(f"ผลลัพธ์: {num1} + {num2} = {result}")
            elif choice == "2":
                result = num1 - num2
                print(f"ผลลัพธ์: {num1} - {num2} = {result}")
            elif choice == "3":
                result = num1 * num2
                print(f"ผลลัพธ์: {num1} * {num2} = {result}")
            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print(f"ผลลัพธ์: {num1} / {num2} = {result}")
                else:
                    print("ข้อผิดพลาด: ไม่สามารถหารด้วยศูนย์ได้")
            elif choice == "5":
                result = num1 ** num2
                print(f"ผลลัพธ์: {num1} ^ {num2} = {result}")
        
        elif choice == "6":
            # คำนวณรากที่สอง
            num = float(input("กรอกตัวเลข: "))
            if num >= 0:
                result = math.sqrt(num)
                print(f"รากที่สองของ {num} คือ {result}")
            else:
                print("ข้อผิดพลาด: ไม่สามารถหารากที่สองของจำนวนลบได้")
        
        elif choice == "7":
            print("ออกจากโปรแกรม.")
            break
        
        else:
            print("เลือกคำสั่งไม่ถูกต้อง. กรุณาลองใหม่.")

# เรียกใช้โปรแกรม
if __name__ == "__main__":
    calculator()
