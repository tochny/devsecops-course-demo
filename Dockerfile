FROM python:3.13-alpine

WORKDIR /app
COPY src/ ./
EXPOSE 8080
USER nobody
CMD ["python", "app.py"]
