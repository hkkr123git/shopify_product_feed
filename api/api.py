from flask import Flask, jsonify, request
from generate import get_csv
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/feed', methods=['POST'])
def feed():
	if not request.json:
		return jsonify({"status": 'error', 'message': 'payload missing'})

	return get_csv(request.json)


app.run()