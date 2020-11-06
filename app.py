from flask import (Flask, render_template, request, jsonify)
import json

app = Flask(__name__)


# Adding/deleting/editing(moving) points on the map
# Adding/editing data related to the points (like in your original forms)
# Storing data about the pickup and delivery orders on the server (you may use just an in-memory storage for demo purposes)
# Presenting overall data from the server on the map
# Presenting detailed information of the order selected on the map
# Matching addresses to locations and vice versa with geocoding and reverse geocoding services

@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        with open('db.json', 'a') as f:
            json.dump(json.dumps(request.method), f)

        return jsonify(request.data)

    if request.method == 'GET':
        return 'dupa'


if __name__ == '__main__':
    app.run()
