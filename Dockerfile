# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Collect static files during build (if needed)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Use gunicorn in production
CMD ["gunicorn", "savannah.wsgi:application", "--bind", "0.0.0.0:8000"]
