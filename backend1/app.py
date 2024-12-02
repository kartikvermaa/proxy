# from flask import Flask, request, jsonify

# app = Flask(name)

# @app.route('/')
# def index():
#     return jsonify({"message": "Welcome to Backend 1"})

# @app.route('/data', methods=['GET'])
# def getdata():
#     return jsonify({"data": "Data from Backend 1"})

# if name == '_main':
#     app.run(host='0.0.0.0', port=5001)


from flask import Flask, request, jsonify

app = Flask(__name__)  # Correctly pass '__name__' here

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Backend 1"})

@app.route('/data', methods=['GET'])
def getdata():
    return jsonify({"data": "Data from Backend 1"})

if __name__ == '__main__':  # Correct check for running as the main program
    app.run(host='0.0.0.0', port=5001)
