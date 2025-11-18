import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def sentiment_vader(text: str):
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        return "positive", compound
    elif compound <= -0.05:
        return "negative", compound
    else:
        return "neutral", compound

if __name__ == "__main__":
    samples = [
        "I love this product, it's fantastic!",
        "It's okay, not great but not terrible.",
        "I hate this. Worst experience ever."
    ]
    for t in samples:
        label, score = sentiment_vader(t)
        print(f"Text: {t}\n -> {label} (score={score})\n")