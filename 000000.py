count = 0
while count <= 9:
    count += 1
    if count == 5: # ตรวจสอบก่อนว่า count เป็น 5 หรือไม่
        continue   # ถ้าใช่ ให้ข้ามไปเริ่มรอบใหม่ทันที
    print(count)   # ถ้าไม่ใช่ 5 จึงจะพิมพ์ค่า count
 
    