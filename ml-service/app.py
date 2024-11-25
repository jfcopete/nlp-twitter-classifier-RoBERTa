#app.py
from fastapi import FastAPI,APIRouter
import uvicorn
from classifier import Classifier
from nlp import sentiment_analysis
from model import Model
import logging
from BaseModels import classify

logging.basicConfig(level=logging.INFO)

# Crear una instancia de FastAPI
app = FastAPI()
router = APIRouter()

@router.get("/")
async def home():
    """This is the home page of the API"""
    return {"message": "Hello World, Welcome to Sentiment Analysis API"}

@router.post("/sentiment_analysis", response_model=classify.ClassifyResponse)
async def analyze(classify_text: classify.ClassifyRequest):
    try:
        text_to_classify = classify_text.text
        result = sentiment_analysis(text_to_classify)
        return result
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return {"error": "An error occurred during sentiment analysis"}
    
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=6000, reload=True)
    
