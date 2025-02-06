# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install flask

# Run the application
CMD ["python", "app.py"]
