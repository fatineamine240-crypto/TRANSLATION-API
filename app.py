from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['GET'])
def translate_text():
    text = request.args.get('text')
    dest = request.args.get('dest', 'en')
    
    if not text:
        return jsonify({"error": "text parameter is required"}), 400
    
    try:
        result = translator.translate(text, dest=dest)
        return jsonify({
            "original_text": text,
            "translated_text": result.text,
            "dest": dest
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
