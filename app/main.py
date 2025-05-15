from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.api.v1.routes import router
from app.core.config import settings
from textblob import TextBlob

app = FastAPI(title=settings.app_name, version=settings.version)
app.include_router(router, prefix="/api/v1")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def analyze(request: Request, text: str = Form(...)):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "text": text,
        "sentiment": sentiment,
        "polarity": polarity
    })