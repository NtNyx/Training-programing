import numpy as np

def solve_linear_equations():
    print("โปรแกรมแก้สมการเชิงเส้น")
    print("1. แก้สมการ 2 ตัวแปร")
    print("2. แก้สมการ 3 ตัวแปร")
    choice = input("เลือกประเภทสมการ (1 หรือ 2): ")

    if choice == "1":
        print("\nสมการ 2 ตัวแปร")
        print("รูปแบบ: a1*x + b1*y = c1 และ a2*x + b2*y = c2")
        
        # รับค่าจากผู้ใช้
        a1, b1, c1 = map(float, input("กรอกค่า a1, b1, c1 (คั่นด้วยช่องว่าง): ").split())
        a2, b2, c2 = map(float, input("กรอกค่า a2, b2, c2 (คั่นด้วยช่องว่าง): ").split())
        
        # สร้างเมทริกซ์
        coefficients = np.array([[a1, b1], [a2, b2]])
        constants = np.array([c1, c2])
        
        try:
            # แก้สมการ
            solution = np.linalg.solve(coefficients, constants)
            print("\nผลลัพธ์:")
            print(f"x = {solution[0]:.2f}, y = {solution[1]:.2f}")
        except np.linalg.LinAlgError:
            print("ไม่สามารถแก้สมการได้ (ระบบสมการอาจไม่มีคำตอบหรือไม่สมบูรณ์)")

    elif choice == "2":
        print("\nสมการ 3 ตัวแปร")
        print("รูปแบบ: a1*x + b1*y + c1*z = d1")
        print("         a2*x + b2*y + c2*z = d2")
        print("         a3*x + b3*y + c3*z = d3")
        
        # รับค่าจากผู้ใช้
        a1, b1, c1, d1 = map(float, input("กรอกค่า a1, b1, c1, d1 (คั่นด้วยช่องว่าง): ").split())
        a2, b2, c2, d2 = map(float, input("กรอกค่า a2, b2, c2, d2 (คั่นด้วยช่องว่าง): ").split())
        a3, b3, c3, d3 = map(float, input("กรอกค่า a3, b3, c3, d3 (คั่นด้วยช่องว่าง): ").split())
        
        # สร้างเมทริกซ์
        coefficients = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
        constants = np.array([d1, d2, d3])
        
        try:
            # แก้สมการ
            solution = np.linalg.solve(coefficients, constants)
            print("\nผลลัพธ์:")
            print(f"x = {solution[0]:.2f}, y = {solution[1]:.2f}, z = {solution[2]:.2f}")
        except np.linalg.LinAlgError:
            print("ไม่สามารถแก้สมการได้ (ระบบสมการอาจไม่มีคำตอบหรือไม่สมบูรณ์)")

    else:
        print("เลือกคำสั่งไม่ถูกต้อง. กรุณาลองใหม่.")

# เรียกใช้โปรแกรม
if __name__ == "__main__":
    solve_linear_equations()
