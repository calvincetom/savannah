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

#5 Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

#6 Copy the source code into the container.
COPY . .

#7 Expose the port that the application listens on.
EXPOSE 8000
