# Sentiment Analyzer API

A simple, containerized **FastAPI** microservice that analyzes the sentiment of input text using `TextBlob`. Built with clean code, modern dev practices, and structured according to the **12-Factor App** principles.

---

## Features

- Sentiment detection: Positive / Negative / Neutral
- Includes automated test with `pytest`
- Dockerized for consistent deployment
- Environment-based configuration using `pydantic.BaseSettings`
- Pre-commit hooks for code quality
- GitHub Actions for CI (tests, linting)
- Well-documented API using FastAPI's built-in docs
---

##  Project Structure

```bash
SentimentAnalyzer/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── main.py
├── tests/
│   └── test_sentiment.py
├── Dockerfile
├── .env
├── .pre-commit-config.yaml
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
├── README.md
```

## Installation & Running

### Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/your-username/sentiment-analyzer.git
cd sentiment-analyzer
```

2. **Install dependencies**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Create a .env file and put this in the file**

```bash
APP_NAME = Sentiment Analyzer
VERSION = 1.0
```

4. **Run the API**

```bash
uvicorn app.main:app --reload
```
### Run With Docker

1. **Build the Docker Image**

```bash
docker build -t sentiment-analyzer
```

2.  **Run the Container**

```bash
docker run -p 8000:8000 --env-file .env sentiment-analyzer
```