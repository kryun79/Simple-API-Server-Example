from flask import Flask, jsonify

server = Flask(__name__)

data = {
  "message": "Welcome!"
}

@server.route('/') # URL
def index():
	return jsonify(data)

@server.route('/2/') # URL
def two():
	return "Route 2!"

server.run(host='0.0.0.0', port=8080)