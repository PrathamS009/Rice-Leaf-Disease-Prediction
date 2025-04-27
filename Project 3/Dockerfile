# Use official Python base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy all files from your local folder to the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "RiceLeafDisease_PreTrained_WebBased.py", "--server.port=8501", "--server.address=0.0.0.0"]
