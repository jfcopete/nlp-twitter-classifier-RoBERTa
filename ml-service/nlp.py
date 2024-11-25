from classifier import Classifier

# Crear una instancia del clasificador
classifier = Classifier()

# Definir una función para realizar el análisis de sentimientos
def sentiment_analysis(text: str):
    # Usar el método del clasificador para analizar el texto
    return classifier.get_sentiment_label_and_score(text)
