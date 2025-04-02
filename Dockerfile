# syntax=docker/dockerfile:1


ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy scripts
COPY scripts/startup.py /app/scripts/
# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Collect static files during build (if needed)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Use gunicorn in production
# CMD ["gunicorn", "savannah.wsgi:application", "--bind", "0.0.0.0:8000"]
# Update CMD
# CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python scripts/startup.py && gunicorn savannah.wsgi:application --bind 0.0.0.0:8000"]
CMD ["sh", "-c", "export DJANGO_SETTINGS_MODULE=savannah.settings && python manage.py makemigrations && python manage.py migrate && python scripts/startup.py && gunicorn savannah.wsgi:application --bind 0.0.0.0:8000"]
