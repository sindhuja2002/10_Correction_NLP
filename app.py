from flask import Flask, request, jsonify
from flask_cors import CORS
from autocorrect import Speller

app = Flask(__name__)
CORS(app)

spell = Speller()

def auto_correct_text(text):
    corrected_text = spell(text)  # Use autocorrect library for simple auto-correction
    return corrected_text

@app.route('/api/autocorrect', methods=['POST'])
def autocorrect():
    data = request.get_json()
    text = data.get('text')

    if text:
        corrected_text = auto_correct_text(text)
        response = {'corrected_text': corrected_text}
        return jsonify(response), 200
    else:
        response = {'error': 'Invalid input'}
        return jsonify(response), 400

if __name__ == '__main__':
    app.run()
