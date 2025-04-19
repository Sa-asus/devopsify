from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data.get('username') == 'admin' and data.get('password') == 'admin':
        return jsonify({"token": "fake-jwt-token"}), 200
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
