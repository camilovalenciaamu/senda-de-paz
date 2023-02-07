FROM python 3.9

RUN pip install Flask gunicorn beautifulsoup4

COPY src/ app/
WORKDIR /app

ENV PORT 8080

