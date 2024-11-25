# nlp.py
from classifier import Classifier

# Crear una instancia del clasificador
classifier = Classifier()

# Definir una función para realizar el análisis de sentimientos
def sentiment_analysis(text: str) -> dict:
    """
    Realiza el análisis de sentimientos en un texto dado.

    Args:
        text (str): El texto que será analizado.

    Returns:
        dict: Un diccionario con la etiqueta ('label') y la puntuación ('score').
    """
    # Utilizar el clasificador para obtener el sentimiento
    sentiment = classifier.get_sentiment_label_and_score(text)
    return sentiment
