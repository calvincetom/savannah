# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started
#1. Base Image
ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-slim AS base 
# Consistent casing for 'AS'

#2. Set Environment Variables
# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

#3. Set work directory
WORKDIR /app

#4 Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001

# # create non-root user
# RUN adduser --disabled-password --gecos "" --uid $UID appuser


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# explicitly install coverage
RUN pip install coverage

#6 Copy the source code into the container.
COPY . .

#7 Expose the port that the application listens on.
EXPOSE 8000

# # CMD TO RUN APP
CMD gunicorn savannah.wsgi:application --bind 0.0.0.0:8000