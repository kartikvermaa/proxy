from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Backend 2"})

@app.route('/data', methods=['GET'])
def getdata():
    return jsonify({"data": "Data from Backend 2"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)