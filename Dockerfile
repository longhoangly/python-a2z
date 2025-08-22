FROM python:3.11-slim

# --------------------------
# 1. Install system packages
# --------------------------
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    default-jre \
    wget \
    ca-certificates \
    gnupg \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libxshmfence1 \
    libxss1 \
    libxtst6 \
    fonts-liberation \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# --------------------------
# 2. Install Allure CLI
# --------------------------
ENV ALLURE_VERSION=2.27.0
RUN curl -L -o allure.zip https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip \
    && unzip allure.zip -d /opt/ \
    && mv /opt/allure-${ALLURE_VERSION} /opt/allure \
    && ln -s /opt/allure/bin/allure /usr/bin/allure \
    && rm allure.zip

# --------------------------
# 3. Set env variables
# --------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# --------------------------
# 4. Install Python deps
# --------------------------
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# --------------------------
# 5. Install Playwright + Browsers
# --------------------------
RUN pip install playwright && playwright install --with-deps

# --------------------------
# 6. Copy all project files
# --------------------------
COPY . /app

# --------------------------
# 7. Create report folders
# --------------------------
RUN mkdir -p reports/allure-results reports/allure-report

# --------------------------
# 8. Default CMD: run tests + generate report
# --------------------------
CMD pytest tests/ --alluredir=reports/allure-results && \
    allure generate reports/allure-results --clean -o reports/allure-report
