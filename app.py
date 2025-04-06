from flask import Flask, jsonify, request

# สร้างแอปพลิเคชัน Flask
app = Flask(__name__)

# Route สำหรับตรวจสอบว่า API ทำงานได้ไหม
@app.route('/')
def home():
    return jsonify(message="Hello, Flask API is working!")

# Route สำหรับ GET request
@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify(message="Hello, welcome to the API!")

# Route สำหรับ POST request
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()  # รับข้อมูลในรูป JSON
    if not data or 'message' not in data:
        return jsonify(error="No message provided"), 400  # ถ้าไม่มีข้อมูล หรือไม่มีฟิลด์ 'message'
    return jsonify(received_message=data['message'])

# เริ่มแอปพลิเคชัน Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
