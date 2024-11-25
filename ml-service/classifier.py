#classifier.py
from scipy.special import softmax
from model import Model
import numpy as np

class Classifier:
    # Constructor: inicializa la clase cargando el modelo y el tokenizer
    def __init__(self)->None:
        # Carga el modelo preentrenado para análisis de sentimientos
        self.model = Model.load_model()
        # Carga el tokenizer asociado al modelo
        self.tokenizer = Model.load_tokenizer()
    
    # Método principal para obtener la etiqueta de sentimiento y su puntuación
    def get_sentiment_label_and_score(self, text:str)->dict:
        # Inicializa un diccionario para almacenar los resultados
        results = {}

        # Define las etiquetas posibles para los sentimientos
        labels = ['negative', 'neutral', 'positive']

        # Tokeniza el texto de entrada y lo convierte en tensores para el modelo
        encoded_input = self.tokenizer(text, return_tensors='pt')

        # Realiza la inferencia con el modelo usando los tensores como entrada
        output = self.model(**encoded_input)

        # Extrae las puntuaciones del modelo, las separa del gráfico computacional y las convierte a un arreglo NumPy
        scores = output[0][0].detach().numpy()

        # Aplica softmax a las puntuaciones para convertirlas en probabilidades
        scores = softmax(scores)

        # Ordena los índices de las probabilidades de menor a mayor
        ranking = np.argsort(scores)

        # Invierte el orden para tener las probabilidades de mayor a menor
        ranking = ranking[::-1]

        # Almacena la etiqueta con mayor puntuación en los resultados
        results['label'] = labels[ranking[0]]

        # Almacena la puntuación de la etiqueta seleccionada, redondeada a 4 decimales
        results['score'] = np.round(scores[ranking[0]], 4)

        # Devuelve el diccionario con la etiqueta y la puntuación
        return results

        