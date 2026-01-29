# Use official python image
FROM python:3.12

# Setup working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run our training script
RUN python model.py

# Expose Port for flask
EXPOSE 5000

# Command to start falsk app
CMD ["python", "app.py"]