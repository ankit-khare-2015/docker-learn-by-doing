# 1) Choose a base image
FROM python:3.11-slim

# 2) Workdir inside the image
WORKDIR /app

# 3) Install deps first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copy source
COPY app.py .

# 5) Expose port and define default command
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
