from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from textblob import TextBlob
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from app.api.v1.routes import router
from app.core.config import settings

import nltk
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

app = FastAPI(title=settings.app_name, version=settings.version)
app.include_router(router, prefix="/api/v1")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

def summarize_text(text):
    # Use the correct Tokenizer for English
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 3)
    return " ".join(str(sentence) for sentence in summary)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
def analyze(request: Request, text: str = Form(...)):
    # Sentiment Analysis
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

    # Text Summarization
    summary = summarize_text(text)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "text": text,
        "sentiment": sentiment,
        "polarity": polarity,
        "summary": summary
    })