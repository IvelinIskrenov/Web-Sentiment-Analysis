from flask import Flask, jsonify, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return jsonify({"error": "Missing 'textToAnalyze' query parameter"}), 400
    # Pass the text to the sentiment_analyzer function and store the response
    try:
        response = sentiment_analyzer(text_to_analyze)
    except Exception as e:
        return jsonify({"error": "Sentiment service error", "detail": str(e)}), 502

    # Extract the label and score from the response
    label = response.get('label')
    score = response.get('score')
    # Return a formatted string with the sentiment label and score
    display_label = label
    if isinstance(label, str) and '_' in label:
        display_label = label.split('_')[-1]


    return jsonify({
        "label": display_label,
        "score": score
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
