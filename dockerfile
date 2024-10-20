# Gunakan image Python sebagai dasar
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Copy semua file ke working directory
COPY . /app

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan bot saat container dimulai
CMD ["python", "bot.py"]
