from flask import Flask, render_template, jsonify, request, json

from modules import extract
from modules import ABREVIACIONES as abr


app = Flask(__name__,
            static_folder='./templates/static',
            template_folder='./templates')


@app.route('/api', methods=['POST'])
def api():
    text = json.loads(request.data)
    types = []

    if text["text"]:
        words = text["text"].split(" ")
        for word in words:
            extraction = extract(word)
            if extraction:
                current_type = map(lambda t: abr.get(t, "No encontrado"),
                                   extraction)
                result = {"text": word, "type": " - ".join(current_type)}
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
