# Use official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies (including Rust)
RUN apt-get update && apt-get install -y cargo

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip

# Ensure dependency compatibility
RUN pip install --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]