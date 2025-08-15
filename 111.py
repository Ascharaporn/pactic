# รับสตริงจากผู้ใช้
text = input("Enter a string: ")

# สร้างตัวแปร 'ธง' เพื่อเก็บสถานะ
has_upper = False
has_lower = False

# วนลูปเพื่อตรวจสอบทีละตัวอักษร
for char in text:
    if char.isupper():
        has_upper = True  # ถ้าเจอตัวพิมพ์ใหญ่ ให้ตั้งธงเป็น True
    elif char.islower():
        has_lower = True  # ถ้าเจอตัวพิมพ์เล็ก ให้ตั้งธงเป็น True

# ตรวจสอบผลลัพธ์จาก 'ธง' ทั้งสอง
if has_upper and has_lower:
    print("The string contains both uppercase and lowercase letters.")
else:
    print("The string does not contain both uppercase and lowercase letters.")

 