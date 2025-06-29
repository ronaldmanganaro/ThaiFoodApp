# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app.py .

# Set environment variables for Streamlit production
ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_WATCH_FILECHANGES=false \
    STREAMLIT_SERVER_ENABLECORS=false \
    STREAMLIT_SERVER_PORT=80 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Expose port 80
EXPOSE 80

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]

