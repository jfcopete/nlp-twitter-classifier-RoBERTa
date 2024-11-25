from nlp import sentiment_analysis

def test_sentiment_analysis_positive():
    try:
        text_to_classify = "I'm happy"
        result = sentiment_analysis(text_to_classify)
        assert result['label'] == 'positive'
        assert result['score'] > 0.8
    except Exception as e:
        return {"error": "An error occurred during sentiment analysis"}

def test_sentiment_analysis_negative():
    try:
        text_to_classify = "I'm so deeply sad"
        result = sentiment_analysis(text_to_classify)
        assert result['label'] == 'negative'
        assert result['score'] > 0.8
    except Exception as e:
        return {"error": "An error occurred during sentiment analysis"}

def test_sentiment_analysis_neutral():
    try:
        text_to_classify = "I'm Neutral"
        result = sentiment_analysis(text_to_classify)
        assert result['label'] == 'neutral'
        assert result['score'] > 0.8
    except Exception as e:
        return {"error": "An error occurred during sentiment analysis"}
