# Use the official Python 3.9 image as the base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py .

# Install Flask and other dependencies
RUN pip install --no-cache-dir flask

# Expose the container port
EXPOSE 5000

# Set the command to run your application
CMD ["python", "app.py"]
