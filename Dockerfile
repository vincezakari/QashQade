# Use the official Python image as base
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Expose port 4004 to the outside world
EXPOSE 4004

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "qashqade_app.py"]

