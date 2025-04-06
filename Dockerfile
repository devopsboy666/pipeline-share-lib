# ใช้ Python 3.8 เป็น base image
FROM python:3.8-slim

# กำหนด directory ภายใน container สำหรับการทำงาน
WORKDIR /app

# คัดลอกไฟล์ requirements.txt เข้าไปใน container
COPY requirements.txt /app/

# ติดตั้ง dependencies จาก requirements.txt
RUN pip install --no-cache-dir -r flask

# คัดลอกไฟล์ทั้งหมดจาก directory ปัจจุบัน (ในเครื่องเรา) ไปยัง /app ใน container
COPY . /app/

# กำหนดพอร์ตที่ Flask จะรัน
EXPOSE 5000

# คำสั่งในการรันแอปพลิเคชัน
CMD ["python", "app.py"]
