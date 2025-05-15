from fastapi import APIRouter
from pydantic import BaseModel
from textblob import TextBlob

router = APIRouter()

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    polarity: float

@router.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(data: TextRequest):
    blob = TextBlob(data.text)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return SentimentResponse(sentiment=sentiment, polarity=polarity)