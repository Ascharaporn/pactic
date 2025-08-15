# รับตัวเลข 3 จำนวนจากผู้ใช้
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# หาตัวเลขที่มากที่สุดโดยใช้ฟังก์ชัน max()
greatest_number = max(num1, num2, num3)

# แสดงผลลัพธ์
print(f"{greatest_number}")