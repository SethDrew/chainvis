
from flask import Flask
from flask import render_template, request, jsonify
from data import get_flip_counts
import json

app = Flask(__name__)


@app.route('/')
def index():
    flips, assignment = get_flip_counts()
    return render_template("index.html", flips=flips)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
    

