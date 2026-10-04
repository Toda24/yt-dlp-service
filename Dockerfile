FROM python:3.10-slim

# Install system dependencies and Deno JavaScript runtime
RUN apt-get update && apt-get install -y curl ffmpeg unzip && rm -rf /var/lib/apt/lists/*
ENV PATH="/root/.deno/bin:$PATH"

# Set working directory
WORKDIR /app

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code and cookies
COPY . .

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
