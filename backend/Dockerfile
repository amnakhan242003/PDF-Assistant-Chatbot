
# FROM python:3.10-slim

# ENV PYTHONUNBUFFERED=1 \
#     PIP_NO_CACHE_DIR=off \
#     TRANSFORMERS_CACHE=/models/transformers \
#     HF_HOME=/models/hf \
#     TORCH_HOME=/models/torch

# WORKDIR /app

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential git curl wget ca-certificates && \
#     rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . .
# RUN mkdir -p /app/uploads /models/transformers /models/hf /models/torch

# EXPOSE 5000

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
