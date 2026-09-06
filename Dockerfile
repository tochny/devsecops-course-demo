FROM python:3.8-slim

WORKDIR /app
COPY src/ ./
EXPOSE 8080
CMD ["python", "app.py"]
