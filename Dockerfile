# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y wget curl unzip fonts-liberation libatk-bridge2.0-0 libgtk-3-0 libnss3 libxss1 libasound2 libxshmfence1 libgbm-dev libdrm2

# Install Playwright
RUN pip install playwright pytest requests

# Download Playwright browsers
RUN playwright install --with-deps

# Copy project files
COPY . .

# Default command
CMD ["pytest", "--headed", "--disable-warnings"]
