from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def urljson():
    if request.method == 'POST':
        # url = request.form['url']
        response = {"url": request.form['url']}

        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
