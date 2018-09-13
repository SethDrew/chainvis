
from flask import Flask
from flask import render_template, request, jsonify
from data import get_flip_totals
import json

app = Flask(__name__)




@app.route('/')
def index():
	flips = get_flip_totals()
	#flips = json.dumps(flips)
	print(flips)
	return render_template("index.html", flips=flips)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
    