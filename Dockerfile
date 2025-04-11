FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libglib2.0-0 libnss3 libgdk-pixbuf2.0-0 libx11-xcb1 libatk-bridge2.0-0 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libgtk-3-0 curl unzip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps chromium

COPY . .
CMD ["python", "-m", "cherryalert.script"]
