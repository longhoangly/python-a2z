FROM mcr.microsoft.com/playwright/python:v1.54.0-jammy

# Set working directory
WORKDIR /app

# Install dependencies including Java for Allure CLI
RUN apt-get update && \
    apt-get install -y wget unzip openjdk-11-jre-headless && \
    rm -rf /var/lib/apt/lists/* && \
    wget -q https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz && \
    tar -xzf allure-2.27.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure && \
    rm allure-2.27.0.tgz

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Default command to run tests and generate report
COPY run-tests.sh /app/run-tests.sh
RUN chmod +x /app/run-tests.sh

# Run tests via entrypoint
ENTRYPOINT ["/app/run-tests.sh"]
