from flask import Flask, request, jsonify, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') # Ensure your HTML file is in a folder named 'templates'

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    review_text = data.get('message', '')

    # NLP Logic: Polarity is -1 (negative) to 1 (positive)
    analysis = TextBlob(review_text)
    score = round(analysis.sentiment.polarity, 2)
    
    if score > 0:
        label = "Positive"
    elif score < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return jsonify(label=label, score=score)

if __name__ == '__main__':
    app.run(debug=True)
