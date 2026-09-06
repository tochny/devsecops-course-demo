FROM python:3.13-slim

WORKDIR /app
COPY src/ ./
EXPOSE 8080
CMD ["python", "app.py"]
