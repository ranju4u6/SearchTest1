# Use Python 3.10 as a base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of your application
COPY . /app

# Expose the port that your app will run on
EXPOSE 5000

# Command to run the Python app
CMD ["python", "app.py"]
