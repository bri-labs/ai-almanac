# Use official python image
FROM python:3.12

# Set working directory inside container
WORKDIR /app

# Install Falsk
RUN pip install Flask

# Copy local files into docker container
COPY app.py .



# EXPOSE port 5000
EXPOSE 6000

# Run flask app
CMD ["python", "app.py"]