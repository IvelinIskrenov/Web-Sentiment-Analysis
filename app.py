from flask import Flask, jsonify, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def render_index_page():
    result = None

    if request.method == "POST":
        
        text = request.form.get("text", "").strip()
        sentiment, score = sentiment_analyzer(text)

        result = {
            "text": text,
            "sentiment": sentiment,
            "score": score
        }

    return jsonify(result)
    #return render_template("index.html", result=result)

if __name__ == "__main__":
    # debug=True helps see request logs; remove in production
    app.run(host="0.0.0.0", port=5000, debug=True)
