# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirments.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirments.txt

# Copy project files
COPY . .

# Expose Flask port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]