from flask import Flask, render_template, jsonify, request, json

from modules import extract


app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    text = json.loads(request.data)
    types = []

    if text["text"]:
        words = text["text"].split(" ")
        for word in words:
            result = {"text": word, "type": extract(word)}
            types.append(result)
    response = {
        'status': '200',
        'types': types
    }
    return jsonify(response)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
